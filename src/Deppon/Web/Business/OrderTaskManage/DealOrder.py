# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def SearchOrder(self,orderno):
    try:
        self.logger.info("开始查询订单......")
        OrderNo = self.browser.find_element_by_name("orderNo")
        OrderNo.send_keys(orderno)
        Search = find_element_by_id_tagename_text(self,"Foss_order_orderHandle_orderHandleQueryForm_Id-innerCt","span","查询")
        Search.click()
        time.sleep(2)
        self.assertRegexpMatches(self.browser.find_element_by_css_selector("BODY").text, r"^[\s\S]*%s[\s\S]*$" % orderno)
        GetOrder = self.browser.find_element_by_css_selector("div.x-grid-row-checker")
        GetOrder.click()
        self.logger.info("查询订单成功......")
        #time.sleep(5)
        #print(self.browser.find_element_by_css_selector("BODY").text, r"^[\s\S]*Y3686[\s\S]*$")
    except Exception as e:
        self.logger.error("查询订单失败......")
        self.logger.error(e)
        raise RuntimeError

def ReturnOrder(self,orderno,reason):
    try:
        SearchOrder(self,orderno)
        self.logger.info("开始退回订单......")
        ReturnOrder = self.browser.find_element_by_xpath("//td[3]/div/img")  #退回订单
        ReturnOrder.click()
        if reason=="地址不详":
            Reason = self.browser.find_element_by_xpath("//td/table/tbody/tr/td[2]/input")#退回原因
            Reason.click()
        else:
            Reason = self.browser.find_element_by_xpath("//td[2]/table/tbody/tr/td[2]/input")
            Reason.click()
            Desc = self.browser.find_element_by_name("desc")
            Desc.send_keys(reason)
        Confirm = self.browser.find_element_by_xpath("//div[2]/div/div/div[2]/div/div/div/em/button")#确认
        Confirm.click()
        try:
            Confirm1 =  ("button-1005-btnInnerEl")
            Confirm1.click()
        except:
            pass
        self.logger.info("退回订单成功......")
    except Exception as e:
        self.logger.error("退回订单失败......")
        self.logger.error(e)
        raise RuntimeError
def DealOrder(self,orderno,vehicleno):
    try:
        SearchOrder(self,orderno)
        #OuterCar = 
        SearchCar = find_element_by_id_tagename_text(self,"T_order-orderHandleIndex_content-body","span","查询车辆")    #点击查询车辆
        SearchCar.click()
        time.sleep(1)
        OuterCar = find_element_by_id_tagename_text(self,"T_order-orderHandleIndex_content-body","span","外请车")    #点击外请车
        OuterCar.click()
        VehicleNo = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        VehicleNo.send_keys(vehicleno,Keys.ENTER)
        time.sleep(2)
        VehicleNo.send_keys(Keys.DOWN)
        time.sleep(2)
        VehicleNo.send_keys(Keys.ENTER)
        time.sleep(2)
        VehicleNo.send_keys(Keys.TAB)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[2]/div[2]/div/div/div[3]/em/button")    
        Search.click()  #点击查询
        GetCar = self.browser.find_element_by_css_selector("div.x-grid-row-radio")#选择车
        GetCar.click()
        Deal = find_element_by_id_tagename_text(self,"T_order-orderHandleIndex_content-body","span","受理")    #点击查询车辆
        Deal.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "受理成功":
            self.logger.info(reslut)
            self.logger.info("受理订单成功......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
    except Exception as e:
        self.logger.error("受理订单失败......")
        self.logger.error(e)
        raise RuntimeError