# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time


def NewUnloadTask(self,platform,billno,employee):
    try:
        self.logger.info("��ʼ��������ж������......")
        UnloadTask = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/em/button")      #����ж������
        UnloadTask.click()
        time.sleep(2)
        BillNo = self.browser.find_element_by_name("billNo")  #���ӵ����
        BillNo.send_keys(billno)
        time.sleep(2)
        Add = self.browser.find_element_by_id("Foss_unload_unloadtaskaddnew_addButton_ID-btnEl") #���
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
        Employee=self.browser.find_element_by_name("loaderCode") #ж��Ա
        Employee.send_keys(employee,Keys.ENTER)
        time.sleep(2)
        Employee.send_keys(Keys.ENTER)
        time.sleep(2)
        Employee.send_keys(Keys.TAB)
        time.sleep(2)
        AddEmployee = self.browser.find_element_by_id("Foss_unload_unloadtaskaddnew_addLoaderButton_ID-btnInnerEl")
        AddEmployee.click()
        time.sleep(2)
        MakeUnloadTask=self.browser.find_element_by_id("Foss_unload_unloadtaskaddnew_saveButton_ID-btnEl")  #����ж������
        MakeUnloadTask.click()
        time.sleep(2)
        TaskCode=self.browser.find_element_by_id("messagebox-1001-displayfield-inputEl").text
        TaskCode=TaskCode.split("��")
        self.logger.info("����ж������ɹ�,������Ϊ: "+TaskCode[1]+"......")
    except:
        self.logger.error("����ж������ʧ��......")
        raise RuntimeError
    return TaskCode[1]
    pass