# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def ConfirmSend(self,billno,begintime,endtime):
    '''
    ����ȷ��
    '''
    try:
        self.logger.info("��ʼ���Գ���ȷ��......")
        BillNo = self.browser.find_element_by_name("billNo")      #���ӵ����
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
        if reslut == "����ȷ�ϳɹ�!":
            self.logger.info(reslut)
            self.logger.info("����ȷ�ϳɹ�......")
        else:
            raise RuntimeError
    except:
        self.logger.info("����ȷ��ʧ��......")
        raise RuntimeError

def ConfirmArrive(self,billno,begintime,endtime):
    '''
    ����ȷ��
    '''
    try:
        self.logger.info("��ʼ���Ե���ȷ��......")
        Tab = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]/div/div[2]/em/button")     #���ﲿ��
        Tab.click()
        time.sleep(2)
        BillNo = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/table/tbody/tr/td[2]/input")      #���ӵ����
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
        Search = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div[3]/em/button")   #��ѯ
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[2]/td/div")
        Checker.click()
        time.sleep(2)
        ConfirmSend = self.browser.find_element_by_xpath("//div[2]/div/div[3]/div/div/div/div/em/button")
        ConfirmSend.click()
        time.sleep(2)
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "����ȷ�ϳɹ�!":
            self.logger.info(reslut)
            self.logger.info("����ȷ�ϳɹ�......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
        
    except:
        self.logger.error("����ȷ��ʧ��......")
        raise RuntimeError