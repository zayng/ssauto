# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def NewFarOffWaybill(self,waybillno,externalbillno,externalusercode,externalagencyfee):
    try:
        self.logger.info("新增偏线外发交接单......")
        AddEir1 = find_element_by_id_tagename_text(self,"T_partialline-index","span","新增")
        AddEir1.click()
        WaybillNo = self.browser.find_element_by_name("waybillNo")
        WaybillNo.send_keys(waybillno)
        ExternalBillNo = self.browser.find_element_by_name("externalBillNo")
        ExternalBillNo.send_keys(externalbillno)
        
        ExternalUserCode = self.browser.find_element_by_name("externalUserCode")
        ExternalUserCode.send_keys(externalusercode,Keys.ENTER)
        time.sleep(2)
        ExternalUserCode.send_keys(Keys.DOWN)
        time.sleep(2)
        ExternalUserCode.send_keys(Keys.ENTER)
        time.sleep(2)
        ExternalUserCode.send_keys(Keys.TAB)
        time.sleep(2)
        

        ExternalAgencyFee = self.browser.find_element_by_name("externalAgencyFee")
        ExternalAgencyFee.clear()
        ExternalAgencyFee.send_keys(externalagencyfee)
        time.sleep(2)
        #DeliveryFee = self.browser.find_element_by_name("deliveryFee")
        #DeliveryFee.send_keys(deliveryfee)
        
        Confirm1 = self.browser.find_element_by_id("Foss_partialline_form_viewpartialline_button_save_Id-btnInnerEl")
        Confirm1.click()
        #time.sleep(1000)
    except:
        self.logger.info("新增偏线外发交接单失败......")
        raise RuntimeError
        