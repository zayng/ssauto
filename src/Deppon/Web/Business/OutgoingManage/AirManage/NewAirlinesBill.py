# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def NewAirlinesBill(self,airlinecomp,airwaybillno,airassembletype,company,flightno,fee,waybill):
    try:
        self.logger.info("新增航空正单......")
        AddBill = find_element_by_id_tagename_text(self,"T_airfreight-airQueryWaybill_content-body","span","新增")
        AddBill.click()
        time.sleep(2)
        AirLineComp = self.browser.find_element_by_xpath("//fieldset/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        AirLineComp.clear()
        AirLineComp.send_keys(airlinecomp,Keys.ENTER)
        time.sleep(2)
        AirLineComp.send_keys(Keys.DOWN)
        time.sleep(2)
        AirLineComp.send_keys(Keys.ENTER)
        time.sleep(2)
        AirLineComp.send_keys(Keys.TAB)
        time.sleep(2)

        AirAssembleType1=self.browser.find_element_by_xpath("//fieldset/div/div/table[5]/tbody/tr/td[2]/table/tbody/tr/td/input")
        AirAssembleType1.click()
        if airassembletype=="单独开单外发":
            AirAssembleType1 = self.browser.find_element_by_xpath("//li[1]")
            AirAssembleType1.click()
        elif airassembletype=="合大票外发":
            AirAssembleType1 = self.browser.find_element_by_xpath("//li[2]")
            AirAssembleType1.click()
        elif airassembletype=="单独开单":
            AirAssembleType1 = self.browser.find_element_by_xpath("//li[3]")
            AirAssembleType1.click()
        elif airassembletype=="合大票":
            AirAssembleType1 = self.browser.find_element_by_xpath("//li[4]")
            AirAssembleType1.click()
        
        AirWaybillNo = self.browser.find_element_by_xpath("//fieldset/div/div/table[2]/tbody/tr/td[2]/input")
        AirWaybillNo.send_keys(airwaybillno)
        time.sleep(2)

        Company = self.browser.find_element_by_name("dedtOrgName")
        Company.clear()
        Company.send_keys(company,Keys.ENTER)
        time.sleep(2)
        Company.send_keys(Keys.DOWN)
        time.sleep(2)
        Company.send_keys(Keys.ENTER)
        Company.send_keys(Keys.TAB)

        
        FlightNo = self.browser.find_element_by_name("flightNo")
        FlightNo.send_keys(flightno,Keys.ENTER)
        time.sleep(2)
        FlightNo.send_keys(Keys.DOWN)
        time.sleep(2)
        FlightNo.send_keys(Keys.ENTER)
        time.sleep(2)
        FlightNo.send_keys(Keys.TAB)
        time.sleep(2)
        
        try:
            self.browser.find_element_by_id("button-1005-btnEl").click()
        except:
            pass

        Add = find_element_by_id_tagename_text(self,"T_airfreight-airEnteringFlightBill_content","span","+")
        Add.click()
        time.sleep(2)
        Ticket = find_element_by_id_tagename_text(self,"T_airfreight-airEnteringFlightBill_content","span","分单合票")
        Ticket.click()
        time.sleep(2)
        '''
        clock = self.browser.find_element_by_xpath("//table[4]/tbody/tr/td[2]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div")
        clock.click()
        time.sleep(4)
        self.browser.switch_to_frame()

        self.browser.find_element_by_css_selector("div.navImg.NavImgl > a").click()
        self.browser.find_element_by_xpath(//*[@id="dpTitle"]/div[2]).click()

        time.sleep(4)
        T = self.browser.find_element_by_xpath(//*[@id="dpClearInput"])
        time.sleep(4)
        T.click()

        time.sleep(10)
        EndTime = self.browser.find_element_by_name("beginInTime")
        EndTime.send_keys("2012")
        '''
        
        self.browser.find_element_by_xpath("//table[4]/tbody/tr/td[2]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div").click()
        clock = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to_frame(clock)
        date = self.browser.find_element_by_id('''dpClearInput''')
        date.click()
        #Confirm1 = self.browser.find_element_by_xpath("//input[@id='dpOkInput']")
        #Confirm1.click()
        self.browser.switch_to_default_content()
        
        time.sleep(2)
        Search = find_element_by_id_tagename_text(self,"window-1430-body","span","查询")
        Search.click()
        time.sleep(2)
        Waybill = self.browser.find_element_by_name("waybillNo")
        Waybill.send_keys(waybill)
        time.sleep(2)
        AddWaybill = find_element_by_id_tagename_text(self,"window-1430-body","span","快速下移")
        AddWaybill.click()
        time.sleep(2)
        SelectAll = self.browser.find_element_by_id("gridcolumn-1435-textEl")
        SelectAll.click()
        time.sleep(2)
        AddWaybill = find_element_by_id_tagename_text(self,"window-1430-body","span","提交合票")
        AddWaybill.click()
        time.sleep(2)
        try:
            self.browser.find_element_by_id("button-1005-btnInnerEl").click()
        except:
            pass
        time.sleep(2)
        Fee = self.browser.find_element_by_name("fee")
        Fee.clear()
        Fee.send_keys(fee)

        time.sleep(2)
        Save = find_element_by_id_tagename_text(self,"T_airfreight-airEnteringFlightBill_content","span","保存")
        Save.click()

        self.logger.info("新增航空正单成功......")
    except:
        raise RuntimeError
        self.logger.info("新增航空正单失败......")