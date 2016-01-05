# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def NotifyCustomer(self,billno):
    try:
        self.logger.info("开始通知客户......")
        BillNo = self.browser.find_element_by_name("waybillNo")      #按运单号查
        BillNo.send_keys(billno)
        time.sleep(60)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[3]/em/button")  #查询
        Search.click()
        time.sleep(2)
        AddNotify1 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/span")#选择
        AddNotify1.click()
        time.sleep(2)
        Notify = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/em/button")
        Notify.click()
        time.sleep(2)
        AddNotify2 = self.browser.find_element_by_xpath('''//div[11]/div[2]/div/div/div/div/div/div/span''')
        AddNotify2.click()
        time.sleep(2)
        Confirm = self.browser.find_element_by_xpath("//div[11]/div[3]/div/div/div/em/button")
        Confirm.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "批量发送至短信平台成功，请稍后查看通知状态。":
            self.logger.info(reslut)
            self.logger.info("结束通知客户......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
    except:
        self.logger.info("通知客户失败......")        
        raise RuntimeError