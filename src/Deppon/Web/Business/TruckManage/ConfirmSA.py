# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def ConfirmSend(self,billno,begintime,endtime):
    '''
    出发确认
    '''
    try:
        self.logger.info("开始测试出发确认......")
        BillNo = self.browser.find_element_by_name("billNo")      #交接单编号
        BillNo.send_keys(billno)
        time.sleep(2)
        BeginTime = self.browser.find_element_by_id("Foss_arrival_QueryDepartureForm_createTime_Id_first-inputEl")
        BeginTime.clear()
        BeginTime.send_keys(begintime)
        time.sleep(2)
        EndTime = self.browser.find_element_by_id("Foss_arrival_QueryDepartureForm_createTime_Id_second-inputEl")
        EndTime.clear()
        EndTime.send_keys(endtime)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]")
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[3]/div/table/tbody/tr[2]/td/div/div")
        Checker.click()
        time.sleep(2)
        ConfirmSend = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/em/button")
        ConfirmSend.click()
        time.sleep(2)
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "发车确认成功!":
            self.logger.info(reslut)
            self.logger.info("出发确认成功......")
        else:
            raise RuntimeError
    except:
        self.logger.info("出发确认失败......")
        raise RuntimeError

def ConfirmArrive(self,billno,begintime,endtime):
    '''
    到达确认
    '''
    try:
        self.logger.info("开始测试到达确认......")
        Tab = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]/div/div[2]/em/button")     #到达部门
        Tab.click()
        time.sleep(2)
        BillNo = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/table/tbody/tr/td[2]/input")      #交接单编号
        BillNo.send_keys(billno)
        time.sleep(2)
        BeginTime = self.browser.find_element_by_id("Foss_arrival_QueryArriveForm_createTime_Id_first-inputEl")
        BeginTime.clear()
        BeginTime.send_keys(begintime)
        time.sleep(2)
        EndTime = self.browser.find_element_by_id("Foss_arrival_QueryArriveForm_createTime_Id_second-inputEl")
        EndTime.clear()
        EndTime.send_keys(endtime)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div[3]/em/button")   #查询
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[2]/td/div")
        Checker.click()
        time.sleep(2)
        ConfirmSend = self.browser.find_element_by_xpath("//div[2]/div/div[3]/div/div/div/div/em/button")
        ConfirmSend.click()
        time.sleep(2)
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "到达确认成功!":
            self.logger.info(reslut)
            self.logger.info("到达确认成功......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
        
    except:
        self.logger.error("到达确认失败......")
        raise RuntimeError