# -*- coding: cp936 -*-
import xlrd
import os
import string
def makeStep(data,readCase,case,getValuerow):
    '''
    解析用例
    '''
    str=""
    FCaseCode=readCase[0]
    FCaseName=readCase[1]
    SCaseCode=readCase[2]
    SCaseName=readCase[3]
    getStep=readCase[5].split("→")      #拆分步骤
    for x in range(len(getStep)):
        getValue=getStep[x].split("::")
        getPar=getValue[1].split("|")       #拆分参数
        par=""
        for i in range(len(getPar)):
            if len(getPar[i].split("#"))==2:
                #print(getPar[i])
                t=getPar[i].split("#")
                row = int(t[1])+ int(getValuerow)-1
                #print(x)
                #print(case.row_values(x)[9])

                getPar[i]="self.GetReturnValue(%s,9)" % row#case.row_values(x)[9]
                #print(getPar[i])
                par=par+getPar[i]+','
            else:
                par=par+'"'+getPar[i]+'",'
        function = data.sheet_by_name("function list")
        for t in range(function.nrows):
            readFunction=function.row_values(t)
            if getValue[0]==readFunction[0]:        #解析函数列表生成函数
                str =str + "\n            " + readFunction[1] % par[0:-1]
    return FCaseCode,SCaseCode,str
def makeUnitest(data,readCase,nrow,case,getValuerow):
    FCaseCode,SCaseCode,oprate=makeStep(data,readCase,case,getValuerow)
    Path=".\Script\\"+FCaseCode
    try:
        #print(Path)
        os.mkdir(Path)
    except:
        pass
    output = open(Path+"\\"+FCaseCode+"_"+SCaseCode+".py", "w")
    output.write('''# -*- coding: cp936 -*-
import os
import sys
os.chdir("..\..")
sys.path.append("C:\workspace\FossAutoTest")

from ModulePackage.Module import * 

class Test(unittest.TestCase):
    global logger
    global judge
    global GetHandOverBillNo
    global TaskCode
    global driver
    logging.config.fileConfig(r"./conf/msg.conf")
    logger = logging.getLogger("FOSS")
    
    def setUp(self):
        self.logger=logger
        self.logger.info("启动测试......")
        self.boolean=True
        self.browser = webdriver.Remote('http://192.168.20.23:8100/wd/hub', DesiredCapabilities.CHROME);
        #self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.set_window_size(1280,700)
        self.browser.set_window_position(0,0)
    
    def tearDown(self):
        time.sleep(5)
        self.browser.quit()
    
    
    def testFoss_'''+FCaseCode+'''(self):
        GetReturn=""
        try:
            '''+oprate+'''
        except:
            self.boolean=False
            raise RuntimeError
        finally:
            if self.boolean==True:
                self.WriteRes('''+str(nrow)+''', 8, "True!")
            else:
                self.WriteRes('''+str(nrow)+''', 8, 'FALSE!')
            if GetReturn !="":
                self.WriteRes('''+str(nrow)+''',9,GetReturn)
            Path=".\ResultPic"+"\\\\"+datetime.datetime.now().strftime('%Y_%m_%d')
            try:
                os.mkdir(Path)
            except:
                pass
            Path=Path+"\\\\'''+FCaseCode+'''"
            Local = Path+"\\\\'''+SCaseCode+'''"+"-"+datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')+".jpg"
            try:
                os.mkdir(Path)
            except:
                pass
            self.browser.save_screenshot(Local)
            
    def GetReturnValue(self,nrow,ncol):
        data = xlrd.open_workbook(".\TestCase\TestCase.xls")
        case = data.sheet_by_name("test case")
        nrows=case.nrows
        return case.row_values(nrow)[ncol]
    
    def WriteRes(self,nrow,ncol,input):
        rb = open_workbook('.\TestCase\TestCase.xls')
        rs = rb.sheet_by_index(0) 
        wb = copyd(rb)
        ws = wb.get_sheet(0)
        ws.write(nrow, ncol, input)
        wb.save('.\TestCase\TestCase.xls')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
''')
    output.close()
if __name__ == '__main__':
    print("正在生成测试脚本......")
    data = xlrd.open_workbook(".\TestCase\TestCase.xls")
    case = data.sheet_by_name("test case")
    nrows=case.nrows
    Fcase=[]
    for i in range(nrows-1):
        row = i+1
        readCase=case.row_values(row)#取Case
        if Fcase!=readCase[0]:
            print(readCase[0],row)
            getValuerow=row       
        Fcase=readCase[0]
        
        makeUnitest(data,readCase,row,case,getValuerow)
        #print(readCase)
    print("生成测试脚本完成......")
    #os.system("pause")