# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def LoadSeal(self,backbillno="",sidebillno=""):
    '''
    װ����ǩ
    '''
    time.sleep(100)
    try:
        self.logger.info("��ʼװ����ǩ......")
        BillNo = self.browser.find_element_by_name("billNo")      #���ӵ����
        BillNo.send_keys(backbillno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div[3]/em/button")        #��ѯ
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/div")       #ѡ���
        Checker.click()
        time.sleep(2)
        BindSeal = self.browser.find_element_by_xpath("//div/div[2]/div/div/div/div/em/button")      #�󶨷�ǩ
        BindSeal.click()
        time.sleep(2)
        AddRow1 = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[4]/div/div/div/em/button")      #�������
        AddRow1.click()             
        time.sleep(2)
        AddNum1 = self.browser.find_element_by_name("sealNo") #�����ǩ
        AddNum1.send_keys(backbillno,Keys.ENTER)
        time.sleep(2)
        AddRow2 = self.browser.find_element_by_xpath("//div[2]/div[4]/div/div/div/em/button")  #�������2
        AddRow2.click()             
        time.sleep(2)
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1150-inputEl") #�����ǩ
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass 
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1151-inputEl") #�����ǩ
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass   
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1156-inputEl") #�����ǩ
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass          
        
        time.sleep(2)
        try:
            Save = self.browser.find_element_by_id("button-1134-btnInnerEl")      #����
            Save.click()
        except:
            pass
        try:
            Save = self.browser.find_element_by_id("button-1133-btnInnerEl")      #����
            Save.click()
        except:
            pass
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "����ɹ�!":
            self.logger.info(reslut)
            self.logger.info("����װ����ǩ......")
        else:
            raise RuntimeError
    except:
        raise RuntimeError
        self.logger.info("װ����ǩʧ��......")
        

def UnloadSeal(self,backbillno="",sidebillno=""):
    '''
    У���ǩ
    '''
    try:
        self.logger.info("��ʼ����У���ǩ......")
        BillNo = self.browser.find_element_by_xpath("//div[2]/div/table/tbody/tr/td[2]/input")      #���ӵ����
        BillNo.send_keys(backbillno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div[2]/div/div[3]")        #��ѯ
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/div")       #ѡ���
        Checker.click()
        time.sleep(2)
        BindSeal = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[2]/em/button")      #У���ǩ
        BindSeal.click()
        time.sleep(2)
        AddRow1 = self.browser.find_element_by_xpath("//div[4]/div/div/div/em/button")      #�������
        AddRow1.click()             
        time.sleep(2)
        AddNum1 = self.browser.find_element_by_name("sealNo") #�����ǩ
        AddNum1.send_keys(backbillno,Keys.ENTER)
        time.sleep(2)
        AddRow2 = self.browser.find_element_by_xpath("//div[2]/div[4]/div/div/div/em/button")  #�������2
        AddRow2.click()
        time.sleep(2)
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1148-inputEl") #�����ǩ
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1149-inputEl") #�����ǩ
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass
        time.sleep(2)
        try:
            Save = self.browser.find_element_by_xpath("//div[3]/div/div/div[2]/em/button")      #����
            Save.click()
        except:
            pass
        try:
            Save = self.browser.find_element_by_xpath("//div/div/div[3]/div/div/div[2]/em/button")      #����
            Save.click()
        except:
            pass       
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "����ɹ�!":
            self.logger.info(reslut)
            self.logger.info("����װ����ǩ......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
    except:
        self.logger.info("У���ǩʧ��......")
        raise RuntimeError
def DelLoadSeal(self,backbillno=""):
    '''
    ɾ����ǩ
    '''
    try:
        self.logger.info("��ʼ����ɾ����ǩ......")
        BillNo = self.browser.find_element_by_xpath("//div[2]/div/table/tbody/tr/td[2]/input")      #���ӵ����
        BillNo.send_keys(backbillno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div[2]/div/div[3]")        #��ѯ
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/div")       #ѡ���
        Checker.click()
        DelLoadSeal = self.browser.find_element_by_xpath("//td[2]/div/img[3]")  #ɾ����ǩ
        DelLoadSeal.click()
        time.sleep(2)
        Confirm = self.browser.find_element_by_id("button-1006-btnInnerEl")
        Confirm.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "��ǩ��ϵɾ���ɹ�.":
            self.logger.info(reslut)
            self.logger.info("����ɾ����ǩ......")
        else:
            raise RuntimeError
    except:
        raise RuntimeError
        self.logger.info("ɾ����ǩʧ��......")