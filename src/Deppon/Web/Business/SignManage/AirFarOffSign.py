# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time


def AirFarOffSign(self,billno,trantype,deliverymanname,identifytype,identifycode):
    try:
        self.logger.info("��ʼ����ƫ��ǩ��......")
        Billno = self.browser.find_element_by_name("waybillNo")      #�˵���
        Billno.send_keys(billno)
        time.sleep(2)
        self.browser.find_element_by_name("productCode").click()
        if trantype == "����ƫ��":
            self.browser.find_element_by_xpath("//li").click()
        elif trantype == "��׼����":
            self.browser.find_element_by_xpath("//li[2]").click()
        Search = find_element_by_id_tagename_text(self,"T_sign-airAgencySignIndex","span","��ѯ")
        Search.click()
        time.sleep(2)
        Select = find_element_by_id_tagename_text(self,"T_sign-airAgencySignIndex","div",billno)
        Select.click()
        time.sleep(2)
        DeliverymanName = self.browser.find_element_by_name("deliverymanName")      
        DeliverymanName.send_keys(deliverymanname)
        IdentifyType = self.browser.find_element_by_name("identifyType")      
        IdentifyType.click()
        
        if identifytype=="���֤":
            self.browser.find_element_by_xpath("//div[10]/div/ul/li").click()
        IdentifyCode = self.browser.find_element_by_name("identifycode")      
        IdentifyCode.send_keys(identifycode)
        
        time.sleep(20)
    except:
        self.logger.error("����ƫ��ǩ��ʧ��......")
        raise RuntimeError