# -*- coding: cp936 -*-
import unittest
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import datetime
import os
import traceback
import logging.config
import logging

from Deppon.Web.Operation.Login import *
from Deppon.Web.Business.LoadManage.LoadSeal import *
from Deppon.Web.Business.LoadManage.EirManage import *
from Deppon.Web.Business.LoadManage.LoadListManage import *
from Deppon.Web.Operation.Navigation import *
from Deppon.Web.Business.TruckManage.ConfirmSA import *
from Deppon.Web.Business.UnloadManage.ConfirmUnloadTask import *
from Deppon.Web.Business.UnloadManage.NewUnloadTask import *
from Deppon.Web.Business.DispatchManage.DispatchPlan.ShortDispatchPlan import *
from Deppon.Web.Business.DispatchManage.DispatchPlan.LongDispatchPlan import *
from Deppon.Web.Business.SendManage.NotifyCustomer import *
from Deppon.Web.Business.SignManage.SignOut.SignSelf import *
from Deppon.Web.Business.SignManage.SettlementGoods import *
from xlutils.copyd import copyd
from xlrd import open_workbook

    
class Test(unittest.TestCase):
    '''
    长途
    '''
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
        self.browser = webdriver.Remote('http://192.168.107.135:8100/wd/hub', DesiredCapabilities.CHROME);
        #self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1280,800)
        self.browser.set_window_position(0,0)
        #time.sleep(2)

    def tearDown(self):
        time.sleep(10)
        self.GetResult()
        Path=".\ResultPic"+"\\"+datetime.datetime.now().strftime('%Y_%m_%d')
        Local = Path+"\\"+"Case_006"+"-"+datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')+".jpg"
        try:
            os.mkdir(Path)
        except:
            pass
        self.browser.save_screenshot(Local)
        #time.sleep(10)
        self.browser.quit()
        self.logger.info("结束测试......")

    def testFoss_Case_001(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill
        global LoadNo
        SeNo1 = "99556189"
        SeNo2 = "99552689"
        waybill = "819202003"
        #GetHandOverBillNo = "00154244"
        #LoadNo = "SHBJ13060202"
        judge=True
        try:
            pass
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","092444","qqqqqq","上海闵行区浦江镇营业部");
            #time.sleep(10);
            Navigation(self,"装车管理-交接单管理");
            #time.sleep(10);
            #GetHandOverBillNo=AddEir(self,"短配交接单","上海转运场","冀A62711","鲍振强",waybill,"2013-06-03 09:37:47");
            GetHandOverBillNo=AddEir(self,"短配交接单","上海转运场","沪B94908","刘洋洋",waybill,"2013-06-03 09:37:47");

            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise
        
    def testFoss_Case_002(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill
        try:
            if judge==False:
                raise
            #time.sleep(60);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","092444","qqqqqq","上海闵行区浦江镇营业部");
            #time.sleep(10);
            Navigation(self,"装车管理-装车封签");
            #time.sleep(10);
            #print(GetHandOverBillNo)
            LoadSeal(self,GetHandOverBillNo,SeNo1);
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise
        
    def testFoss_Case_003(self): 
        global judge
        global GetHandOverBillNo
        global TaskCode             
        global SeNo1
        global SeNo2
        global waybill
        try:
            if judge==False:
                raise
            ##time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","092444","qqqqqq","上海闵行区浦江镇营业部");
            ##time.sleep(10);
            Navigation(self,"车辆管理-出发到达确认");
            #time.sleep(10);
            ConfirmSend(self,GetHandOverBillNo,"2013-06-01 00:00:00","2013-06-03 23:59:59");
            
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise

    def testFoss_Case_004(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill                     
        try:
            if judge==False:
                raise            
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"车辆管理-出发到达确认");
            #time.sleep(10);
            ConfirmArrive(self,GetHandOverBillNo,"2013-06-01 00:00:00","2013-06-03 23:59:59");
            
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise
        
    def testFoss_Case_005(self):
        global judge
        global GetHandOverBillNo
        global TaskCode 
        global SeNo1
        global SeNo2
        global waybill    
        try:
            if judge==False:
                raise
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-装车封签");
            #time.sleep(10);
            UnloadSeal(self,GetHandOverBillNo,SeNo1);
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise
        
    def testFoss_Case_006(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill
        try:
            if judge==False:
                raise            
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"卸车管理-查询卸车任务");
            #time.sleep(10);
            TaskCode=NewUnloadTask(self,"001",GetHandOverBillNo,"王成法");
            #time.sleep(5)
            
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise
        
    def testFoss_Case_007(self):    
        global judge
        global GetHandOverBillNo
        global TaskCode 
        global SeNo1
        global SeNo2
        global waybill  
        try:
            if judge==False:
                raise            
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"卸车管理-查询卸车任务");
            #time.sleep(10);
            ConfirmUnloadTask(self,TaskCode);
            
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise
    
    def testFoss_Case_008(self): 
        global judge
        global GetHandOverBillNo
        global TaskCode 
        global SeNo1
        global SeNo2
        global waybill       
        try:
            if judge==False:
                raise            
            #time.sleep(5);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(5);
            Navigation(self,"调度管理-发车计划-长途发车计划");
            #time.sleep(5);
            NewLongDispatchPlan(self,"2013-06-03","上海转运场","北京转运场");
            #time.sleep(5)
            MakeLongDispatchPlanInCar(self,"北京车队城区内环接送货组","京E64933","2013-06-03 09:09:09","2013-06-03 09:09:09","2013-06-03 09:09:09","北京车队城区内环接送货组","刘得松")
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise
        
    def testFoss_Case_009(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-交接单管理");
            #time.sleep(10);
            GetHandOverBillNo=AddEir(self,"集配交接单","北京转运场","京E64933","刘得松",waybill,"2013-06-03 09:37:47");

            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise        
    
    def testFoss_Case_010(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global LoadNo
        global SeNo1
        global SeNo2
        global waybill

        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-配载单管理");
            #time.sleep(10);
            LoadNo=NewLoadList(self,"专线","北京转运场","京E64933","精准卡航",GetHandOverBillNo);

            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise 
    
    def testFoss_Case_011(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global LoadNo
        global SeNo1
        global SeNo2
        global waybill   

        try:
            if judge==False:
                raise RuntimeError
            #time.sleep(60);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-装车封签");
            #time.sleep(10);
            print(GetHandOverBillNo)
            LoadSeal(self,GetHandOverBillNo,SeNo2);
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_012(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill  
        try:
            if judge==False:
                raise RuntimeError
            ##time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            ##time.sleep(10);
            Navigation(self,"车辆管理-出发到达确认");
            #time.sleep(10);
            ConfirmSend(self,GetHandOverBillNo,"2013-06-01 00:00:00","2013-06-03 23:59:59");
            
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError

    def testFoss_Case_013(self):
        global judge
        global GetHandOverBillNo
        global TaskCode 
        global SeNo1
        global SeNo2
        global waybill            
        try:
            if judge==False:
                raise RuntimeError            
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001235","qqqqqq","北京转运场");
            #time.sleep(10);
            Navigation(self,"车辆管理-出发到达确认");
            #time.sleep(10);
            ConfirmArrive(self,GetHandOverBillNo,"2013-06-01 00:00:00","2013-06-03 23:59:59");
            
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_014(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global SeNo1
        global SeNo2
        global waybill             
        try:
            if judge==False:
                raise RuntimeError
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001235","qqqqqq","北京转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-装车封签");
            #time.sleep(10);
            UnloadSeal(self,GetHandOverBillNo,SeNo2);
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_015(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        global LoadNo
        global SeNo1
        global SeNo2
        global waybill 
                
        try:
            if judge==False:
                raise RuntimeError           
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001235","qqqqqq","北京转运场");
            #time.sleep(10);
            Navigation(self,"卸车管理-查询卸车任务");
            #time.sleep(10);
            TaskCode=NewUnloadTask(self,"001",LoadNo,"李何友");
            #time.sleep(5)
            
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_016(self):    
        global judge
        global GetHandOverBillNo
        global TaskCode 
        global SeNo1
        global SeNo2
        global waybill      
        try:
            if judge==False:
                raise RuntimeError            
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001235","qqqqqq","北京转运场");
            #time.sleep(10);
            Navigation(self,"卸车管理-查询卸车任务");
            #time.sleep(10);
            ConfirmUnloadTask(self,TaskCode);
            
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise RuntimeError

    def testFoss_Case_017(self):
        global judge
        global GetHandOverBillNo
        global TaskCode 
        global SeNo1
        global SeNo2
        global waybill        
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","097725","qqqqqq","北京派送中心");
            #time.sleep(10);
            Navigation(self,"派送管理-通知客户");
            #time.sleep(10);
            NotifyCustomer(self,waybill);
            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError

    def testFoss_Case_018(self):
        global judge
        global GetHandOverBillNo
        global TaskCode  
        global SeNo1
        global SeNo2
        global waybill           
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","097725","qqqqqq","北京派送中心")
            #time.sleep(10);
            Navigation(self,"签收管理-结清货款")
            #time.sleep(10);
            SettlementGoods(self,waybill,"天天","110101198812012773",0,600,"qqqqqq")
            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
    
    def testFoss_Case_019(self):
        global judge
        global GetHandOverBillNo
        global TaskCode  
        global SeNo1
        global SeNo2
        global waybill           
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","097725","qqqqqq","北京派送中心");
            #time.sleep(10);
            Navigation(self,"签收管理-签收出库-自提签收");
            #time.sleep(10);
            SignSelf(self,waybill);
            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def GetResult(self):
        rb = open_workbook('.\TestCase\TestCase.xls')
        rs = rb.sheet_by_index(0)
        wb = copyd(rb)
        ws = wb.get_sheet(0)
        if self.boolean==True:
            ws.write(6, 6, 'TRUE!')
        else:
            ws.write(6, 6, 'FALSE!')
        wb.save('.\TestCase\TestCase.xls')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()

    suite.addTest(Test("testFoss_Case_001"))
    suite.addTest(Test("testFoss_Case_002"))
    suite.addTest(Test("testFoss_Case_003"))
    suite.addTest(Test("testFoss_Case_004"))
    suite.addTest(Test("testFoss_Case_005"))
    suite.addTest(Test("testFoss_Case_006"))
    suite.addTest(Test("testFoss_Case_007"))
    suite.addTest(Test("testFoss_Case_008"))
    suite.addTest(Test("testFoss_Case_009"))
    suite.addTest(Test("testFoss_Case_010"))
    suite.addTest(Test("testFoss_Case_011"))
    suite.addTest(Test("testFoss_Case_012"))
    suite.addTest(Test("testFoss_Case_013"))
    suite.addTest(Test("testFoss_Case_014"))
    suite.addTest(Test("testFoss_Case_015"))
    suite.addTest(Test("testFoss_Case_016"))
    suite.addTest(Test("testFoss_Case_017"))
    suite.addTest(Test("testFoss_Case_018"))
    suite.addTest(Test("testFoss_Case_019"))

    
    runner = unittest.TextTestRunner()
    runner.run(suite)
