# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def SignSelf(self,billno):
    try:
        self.logger.info("开始客户自提签收......")
        Billno = self.browser.find_element_by_name("waybillNo")      #运单号
        Billno.send_keys(billno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[3]/em/button")      #查询
        Search.click()
        time.sleep(2)
        Sign = self.browser.find_element_by_xpath('''//div[2]/div[3]/div/table/tbody/tr[2]/td/div/img''')       #签收
        Sign.click()
        time.sleep(2)
        SignThing = self.browser.find_element_by_xpath("//div[2]/div[2]/div[2]/div/div/div/div/span")#全选件数
        SignThing.click()
        time.sleep(2)
        try:
            Confirm1 = self.browser.find_element_by_id("button-1104-btnEl")#确认
            Confirm1.click()
        except:
            pass
        try:
            Confirm2 = self.browser.find_element_by_id("button-1105-btnEl")#确认
            Confirm2.click()
        except:
            pass
        time.sleep(2)
        Confirm2 = self.browser.find_element_by_id("button-1006-btnInnerEl")#确认
        Confirm2.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "签收出库成功！发货人短信，收货人短信，在线通知都发送成功！":
            self.logger.info(reslut)
            self.logger.info("结束自提签收......")
        else:
            raise RuntimeError
    except:
        self.logger.error("自提签收失败......")
        raise RuntimeError
    