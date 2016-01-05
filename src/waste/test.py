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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



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

def GetReturnValue(self,nrow,ncol):
    data = xlrd.open_workbook(".\TestCase\TestCase.xls")
    case = data.sheet_by_name("test case")
    nrows=case.nrows
    return case.row_values(nrow)[ncol]


class Test(unittest.TestCase):

    global logger
    global GetHandOverBillNo
    global driver
    logging.config.fileConfig(r"./conf/msg.conf")
    logger = logging.getLogger("FOSS")
  
    def setUp(self):
        print("start")
        self.logger=logger
       
        self.browser = webdriver.Remote('http://192.168.107.133:4444/wd/hub', DesiredCapabilities.CHROME)
        self.browser.implicitly_wait(10)
        pass


    def tearDown(self):
        print("end")
        self.browser.quit()
        pass


    def testName1(self):
        time.sleep(100)
        #Login(self,"http://192.168.10.50/stl-web/login/index.action","074932","qqqqqq","上海青浦重固营业部");
        #Login(self,"http://192.168.10.50/stl-web/login/index.action","001321","qqqqqq","上海转运场");
        #time.sleep(10);
        #Navigation(self,"装车管理-配载单管理");
        #time.sleep(10);
        #LoadNo=NewLoadList(self,"专线","北京转运场","京E64933","精准卡航","");


        pass
        

    def testName2(self):
        Login(self,"http://192.168.10.50/stl-web/login/index.action","074932","qqqqqq","上海青浦重固营业部");
        pass

if __name__ == "__main__":
    #for i in range(2):
    '''
    global GetHandOverBillNo
        #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTest(Test("testName1"))
    suite.addTest(Test("testName2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #print(str(int(random.random()*100000000)))
    print("\u7b2c\u56db\u4ee3\u8425\u8fd0\u652f\u6491\u7cfb\u7edf")'''
    print(GetReturnValue("",1,9))
        