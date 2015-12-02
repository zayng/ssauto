# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def LoadSeal(self,backbillno="",sidebillno=""):
    '''
    装车封签
    '''
    time.sleep(100)
    try:
        self.logger.info("开始装车封签......")
        BillNo = self.browser.find_element_by_name("billNo")      #交接单编号
        BillNo.send_keys(backbillno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div[3]/em/button")        #查询
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/div")       #选择框
        Checker.click()
        time.sleep(2)
        BindSeal = self.browser.find_element_by_xpath("//div/div[2]/div/div/div/div/em/button")      #绑定封签
        BindSeal.click()
        time.sleep(2)
        AddRow1 = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[4]/div/div/div/em/button")      #点击增加
        AddRow1.click()             
        time.sleep(2)
        AddNum1 = self.browser.find_element_by_name("sealNo") #输入封签
        AddNum1.send_keys(backbillno,Keys.ENTER)
        time.sleep(2)
        AddRow2 = self.browser.find_element_by_xpath("//div[2]/div[4]/div/div/div/em/button")  #点击增加2
        AddRow2.click()             
        time.sleep(2)
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1150-inputEl") #输入封签
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass 
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1151-inputEl") #输入封签
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass   
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1156-inputEl") #输入封签
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass          
        
        time.sleep(2)
        try:
            Save = self.browser.find_element_by_id("button-1134-btnInnerEl")      #保存
            Save.click()
        except:
            pass
        try:
            Save = self.browser.find_element_by_id("button-1133-btnInnerEl")      #保存
            Save.click()
        except:
            pass
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "保存成功!":
            self.logger.info(reslut)
            self.logger.info("结束装车封签......")
        else:
            raise RuntimeError
    except:
        raise RuntimeError
        self.logger.info("装车封签失败......")
        

def UnloadSeal(self,backbillno="",sidebillno=""):
    '''
    校验封签
    '''
    try:
        self.logger.info("开始测试校验封签......")
        BillNo = self.browser.find_element_by_xpath("//div[2]/div/table/tbody/tr/td[2]/input")      #交接单编号
        BillNo.send_keys(backbillno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div[2]/div/div[3]")        #查询
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/div")       #选择框
        Checker.click()
        time.sleep(2)
        BindSeal = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[2]/em/button")      #校验封签
        BindSeal.click()
        time.sleep(2)
        AddRow1 = self.browser.find_element_by_xpath("//div[4]/div/div/div/em/button")      #点击增加
        AddRow1.click()             
        time.sleep(2)
        AddNum1 = self.browser.find_element_by_name("sealNo") #输入封签
        AddNum1.send_keys(backbillno,Keys.ENTER)
        time.sleep(2)
        AddRow2 = self.browser.find_element_by_xpath("//div[2]/div[4]/div/div/div/em/button")  #点击增加2
        AddRow2.click()
        time.sleep(2)
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1148-inputEl") #输入封签
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass
        try:
            AddNum2 = self.browser.find_element_by_id("textfield-1149-inputEl") #输入封签
            AddNum2.send_keys(sidebillno,Keys.ENTER)
        except:
            pass
        time.sleep(2)
        try:
            Save = self.browser.find_element_by_xpath("//div[3]/div/div/div[2]/em/button")      #保存
            Save.click()
        except:
            pass
        try:
            Save = self.browser.find_element_by_xpath("//div/div/div[3]/div/div/div[2]/em/button")      #保存
            Save.click()
        except:
            pass       
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "保存成功!":
            self.logger.info(reslut)
            self.logger.info("结束装车封签......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
    except:
        self.logger.info("校验封签失败......")
        raise RuntimeError
def DelLoadSeal(self,backbillno=""):
    '''
    删除封签
    '''
    try:
        self.logger.info("开始测试删除封签......")
        BillNo = self.browser.find_element_by_xpath("//div[2]/div/table/tbody/tr/td[2]/input")      #交接单编号
        BillNo.send_keys(backbillno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div[2]/div/div[3]")        #查询
        Search.click()
        time.sleep(2)
        Checker = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/div")       #选择框
        Checker.click()
        DelLoadSeal = self.browser.find_element_by_xpath("//td[2]/div/img[3]")  #删除分签
        DelLoadSeal.click()
        time.sleep(2)
        Confirm = self.browser.find_element_by_id("button-1006-btnInnerEl")
        Confirm.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "封签关系删除成功.":
            self.logger.info(reslut)
            self.logger.info("结束删除封签......")
        else:
            raise RuntimeError
    except:
        raise RuntimeError
        self.logger.info("删除封签失败......")