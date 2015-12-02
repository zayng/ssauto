# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def ConfirmUnloadTask(self,taskcode):
    try:
        self.logger.info("开始测试确认卸车任务......")
        TaskCode = self.browser.find_element_by_name("unloadTaskNo")      #任务编号
        TaskCode.send_keys(taskcode)
        time.sleep(2)
        Search =  self.browser.find_element_by_xpath("//div[2]/div/div[3]/em/button")     #查询
        Search.click()
        time.sleep(2)
        Confirm1 = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td/div/img")
        Confirm1.click()
        time.sleep(2)
        try:
            Confirm2 = self.browser.find_element_by_id("Foss_unload_unloadtaskconfirm__confirmButton_ID-btnEl")      #确认卸车
            Confirm2.click()
        except:
            pass
        try:
            Confirm2 = self.browser.find_element_by_id("Foss_unload_unloadtaskconfirmlong__confirmButton_ID-btnInnerEl")    #确认卸车
            Confirm2.click()
        except:
            pass
        time.sleep(2)#test
        Confirm3 = self.browser.find_element_by_id("button-1006-btnInnerEl")
        Confirm3.click()
        Confirm4 = self.browser.find_element_by_id("messagebox-1001-displayfield-inputEl").text
        self.logger.info("确认卸车任务成功......")
    except:
        self.logger.error("确认卸车任务失败......")
        raise RuntimeError
    time.sleep(2)