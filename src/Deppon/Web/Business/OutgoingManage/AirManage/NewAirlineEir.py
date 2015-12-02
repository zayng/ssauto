# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def NewAirlineEir(self,flightno,handoveremp,airwaybillno):
    try:
        self.logger.info("新增航空正单交接单......")
        AddEir1 = find_element_by_id_tagename_text(self,"T_airfreight-airHandOverBillIndex","span","新增")
        AddEir1.click()
        time.sleep(2)
        FlightNo = self.browser.find_element_by_xpath("//div[2]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input")
        FlightNo.send_keys(flightno,Keys.ENTER)
        time.sleep(2)
        FlightNo.send_keys(Keys.DOWN)
        time.sleep(2)
        FlightNo.send_keys(Keys.ENTER)
        time.sleep(2)
        FlightNo.send_keys(Keys.TAB)
        time.sleep(2)
        
        HandoverEmp = self.browser.find_element_by_name("handoverEmp")
        HandoverEmp.send_keys(handoveremp,Keys.ENTER)
        time.sleep(2)
        HandoverEmp.send_keys(Keys.DOWN)
        time.sleep(2)
        HandoverEmp.send_keys(Keys.ENTER)
        time.sleep(2)
        HandoverEmp.send_keys(Keys.TAB)
        time.sleep(2)
        
        AirWaybillNo = self.browser.find_element_by_xpath("//div[4]/div/div/table[2]/tbody/tr/td[2]/input")
        AirWaybillNo.send_keys(airwaybillno)
        time.sleep(2)
        AddEir2 = self.browser.find_element_by_id("button-1090-btnInnerEl")
        AddEir2.click()
        time.sleep(2)
        SelectAll = self.browser.find_element_by_id("gridcolumn-1162-textEl")
        SelectAll.click()
        time.sleep(2)
        Save = self.browser.find_element_by_id("button-1118-btnInnerEl")
        Save.click()
        self.logger.info("新增航空正单交接单成功......")
    except:
        raise RuntimeError
        self.logger.error("新增航空正单交接单失败......")