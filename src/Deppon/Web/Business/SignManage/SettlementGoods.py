# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def SettlementGoods(self,billno,name,certificate,actualfreight,codamount,passwd):
    try:
        self.logger.info("开始结清货款......")
        Billno = self.browser.find_element_by_name("waybillNo")      #运单号
        Billno.send_keys(billno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[3]/em/button")
        Search.click()
        time.sleep(2)    
        GetMsg = self.browser.find_element_by_xpath('''//tr[2]/td[2]/div''')
        GetMsg.click()
        time.sleep(2)
        Name = self.browser.find_element_by_name("deliverymanName")
        Name.clear()
        Name.send_keys(name)
        time.sleep(2)
        Certificate = self.browser.find_element_by_name("identifyCode")
        Certificate.send_keys(certificate)
        time.sleep(2)
        actualFreight = self.browser.find_element_by_name("actualFreight")
        actualFreight.clear()
        actualFreight.send_keys(actualfreight)
        time.sleep(2)
        try:
            codAmount = self.browser.find_element_by_name("codAmount")
            codAmount.clear()
            codAmount.send_keys(codamount)
            time.sleep(2)
        except:
            pass
        Confirm1 = self.browser.find_element_by_id("Foss_sign_settlePayment_Payment_Id-btnInnerEl")
        Confirm1.click()
        try:
            ConfirmPwd = self.browser.find_element_by_name("cancelarea-inputEl")
            ConfirmPwd.send_keys(passwd)
            time.sleep(2)
            Confirm2 = self.browser.find_element_by_id("button-1067-btnInnerEl")
            Confirm2.click()
        except:
            pass
        self.logger.info("结束结清货款......")
        time.sleep(2)
    except:
        self.logger.info("结清货款失败......")
        raise RuntimeError
