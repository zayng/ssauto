# -*- coding: cp936 -*-
import unittest
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
import traceback
import logging.config
import logging

from Deppon.Web.Operation.Login import *
from Deppon.Web.Business.LoadManage.LoadSeal import *
from Deppon.Web.Business.LoadManage.EirManage import *
from Deppon.Web.Operation.Navigation import *
from Deppon.Web.Business.TruckManage.ConfirmSA import *
from Deppon.Web.Business.UnloadManage.ConfirmUnloadTask import *
from Deppon.Web.Business.UnloadManage.NewUnloadTask import *
from Deppon.Web.Business.DispatchManage.DispatchPlan.ShortDispatchPlan import *
from Deppon.Web.Business.SendManage.NotifyCustomer import *
from Deppon.Web.Business.SignManage.SignOut.SignSelf import *
from Deppon.Web.Business.SignManage.SettlementGoods import *
from xlutils.copyd import copyd
from xlrd import open_workbook

    
class Test(unittest.TestCase):
    '''
    短途
    '''
    global logger
    global judge
    global GetHandOverBillNo
    global TaskCode
    logging.config.fileConfig(r"./conf/msg.conf")
    logger = logging.getLogger("FOSS")
    def setUp(self):
        self.logger=logger
        self.logger.info("启动测试......")
        self.boolean=True
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1280,1000)
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
        judge=True
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","074932","qqqqqq","上海青浦重固营业部");
            #time.sleep(10);
            Navigation(self,"装车管理-交接单管理");
            #time.sleep(10);
            GetHandOverBillNo=AddEir(self,"短配交接单","上海转运场","冀A62711","鲍振强","931987500","2013-06-04 09:37:47");

            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_002(self):
        global judge
        global GetHandOverBillNo
        global TaskCode        
        try:
            if judge==False:
                raise RuntimeError
            #time.sleep(60);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","074932","qqqqqq","上海青浦重固营业部");
            #time.sleep(10);
            Navigation(self,"装车管理-装车封签");
            #time.sleep(10);
            print(GetHandOverBillNo)
            LoadSeal(self,GetHandOverBillNo,"00333859");
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_003(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            if judge==False:
                raise RuntimeError
            ##time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","074932","qqqqqq","上海青浦重固营业部");
            ##time.sleep(10);
            Navigation(self,"车辆管理-出发到达确认");
            #time.sleep(10);
            ConfirmSend(self,GetHandOverBillNo,"2013-06-01 00:00:00","2013-06-04 23:59:59");
            
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError

    def testFoss_Case_004(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            if judge==False:
                raise RuntimeError            
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"车辆管理-出发到达确认");
            #time.sleep(10);
            ConfirmArrive(self,GetHandOverBillNo,"2013-06-01 00:00:00","2013-06-04 23:59:59");
            
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_005(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            if judge==False:
                raise RuntimeError
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-装车封签");
            #time.sleep(10);
            UnloadSeal(self,GetHandOverBillNo,"00333859");
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_006(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            if judge==False:
                raise RuntimeError           
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
            raise RuntimeError
        
    def testFoss_Case_007(self):    
        global judge
        global GetHandOverBillNo
        global TaskCode               
        try:
            if judge==False:
                raise RuntimeError            
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
            raise RuntimeError
    
    def testFoss_Case_008(self): 
        global judge
        global GetHandOverBillNo
        global TaskCode                 
        try:
            if judge==False:
                raise RuntimeError            
            #time.sleep(5);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(5);
            Navigation(self,"调度管理-发车计划-短途发车计划");
            #time.sleep(5);
            NewShortDispatchPlan(self,"2013-06-04","上海转运场","上海派送中心");
            #time.sleep(5)
            MakeShortDispatchPlanInCar(self,"上海宝山区车队","沪B99495","上海宝山区车队","周微")
        except:
            traceback.print_exc()
            self.judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_009(self):
        global judge
        global GetHandOverBillNo
        global TaskCode
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
            #time.sleep(10);
            Navigation(self,"装车管理-交接单管理");
            #time.sleep(10);
            GetHandOverBillNo=AddEir(self,"短配交接单","上海派送中心","沪B99495","周微","931987500","2013-06-04 09:37:47");
            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError

    def testFoss_Case_010(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","092312","qqqqqq","上海派送中心");
            #time.sleep(10);
            Navigation(self,"派送管理-通知客户");
            #time.sleep(10);
            NotifyCustomer(self,"931987500");
            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_011(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","092312","qqqqqq","上海派送中心");
            #time.sleep(10);
            Navigation(self,"签收管理-结清货款");
            #time.sleep(10);
            SettlementGoods(self,"931987500","天天","110101198812012773");
            #print(GetHandOverBillNo)
        except:
            traceback.print_exc()
            judge=False
            self.boolean=False
            raise RuntimeError
        
    def testFoss_Case_012(self):
        global judge
        global GetHandOverBillNo
        global TaskCode             
        try:
            #time.sleep(10);
            Login(self,"http://192.168.10.50/stl-web/login/index.action","092312","qqqqqq","上海派送中心");
            #time.sleep(10);
            Navigation(self,"签收管理-签收出库-自提签收");
            #time.sleep(10);
            SignSelf(self,"931987500");
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

    runner = unittest.TextTestRunner()
    runner.run(suite)
