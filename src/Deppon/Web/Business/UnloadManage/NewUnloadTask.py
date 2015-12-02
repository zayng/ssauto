# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time


def NewUnloadTask(self,platform,billno,employee):
    try:
        self.logger.info("开始测试新增卸车任务......")
        UnloadTask = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/em/button")      #新增卸车任务
        UnloadTask.click()
        time.sleep(2)
        BillNo = self.browser.find_element_by_name("billNo")  #交接单编号
        BillNo.send_keys(billno)
        time.sleep(2)
        Add = self.browser.find_element_by_id("Foss_unload_unloadtaskaddnew_addButton_ID-btnEl") #添加
        Add.click()
        time.sleep(2)
        if platform!="":
            Platform = self.browser.find_element_by_name("platformCode")
            Platform.send_keys(platform,Keys.ENTER)
            time.sleep(2)
            Platform.send_keys(Keys.DOWN)
            time.sleep(2)
            Platform.send_keys(Keys.ENTER)
            time.sleep(2)
            Platform.send_keys(Keys.TAB)
            time.sleep(2)
        Employee=self.browser.find_element_by_name("loaderCode") #卸车员
        Employee.send_keys(employee,Keys.ENTER)
        time.sleep(2)
        Employee.send_keys(Keys.ENTER)
        time.sleep(2)
        Employee.send_keys(Keys.TAB)
        time.sleep(2)
        AddEmployee = self.browser.find_element_by_id("Foss_unload_unloadtaskaddnew_addLoaderButton_ID-btnInnerEl")
        AddEmployee.click()
        time.sleep(2)
        MakeUnloadTask=self.browser.find_element_by_id("Foss_unload_unloadtaskaddnew_saveButton_ID-btnEl")  #生成卸车任务
        MakeUnloadTask.click()
        time.sleep(2)
        TaskCode=self.browser.find_element_by_id("messagebox-1001-displayfield-inputEl").text
        TaskCode=TaskCode.split("：")
        self.logger.info("新增卸车任务成功,任务编号为: "+TaskCode[1]+"......")
    except:
        self.logger.error("新增卸车任务失败......")
        raise RuntimeError
    return TaskCode[1]
    pass