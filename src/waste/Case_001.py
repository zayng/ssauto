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
        #self.browser = webdriver.Remote('http://192.168.107.133:4444/wd/hub', DesiredCapabilities.CHROME);
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1280,700)
        self.browser.set_window_position(0,0)
    
    def tearDown(self):
        time.sleep(10)
        self.browser.quit()
    
    
    def testFoss_Case_001(self):
        try:
            print("-")
            #Login(self,"http://192.168.10.50/stl-web/login/index.action","074932","qqqqqq","上海青浦重固营业部")
            #Navigation(self,"装车管理-交接单管理")
            #AddEir(self,"短配交接单","上海转运场","沪D02018","刘得松","931987392","2013-05-22 09:37:47")
        except:
            self.boolean=False
            raise RuntimeError
        finally:
            if self.boolean==True:
                self.WirteRes(1, 6, "True!")
            else:
                self.WirteRes(1, 6, 'FALSE!')
            Path=".\ResultPic"+"\\"+datetime.datetime.now().strftime('%Y_%m_%d')
            Local = Path+"\\"+"Case_001"+"-"+datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')+".jpg"
            try:
                os.mkdir(Path)
            except:
                pass
            self.browser.save_screenshot(Local)
            

    def WirteRes(self,nrow,ncol,input):
        rb = open_workbook('.\TestCase\TestCase.xls')
        rs = rb.sheet_by_index(0) 
        wb = copyd(rb)
        ws = wb.get_sheet(0)
        ws.write(nrow, ncol, input)
        wb.save('.\TestCase\TestCase.xls')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
