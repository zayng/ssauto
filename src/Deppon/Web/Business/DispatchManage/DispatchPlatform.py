# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def SearchPlatform(self,platformno):
    try:
        self.logger.info("开始查询月台......")
        StartPlatformCode = self.browser.find_element_by_name("startPlatformCode")
        StartPlatformCode.send_keys(platformno,Keys.ENTER)
        time.sleep(2)
        StartPlatformCode.send_keys(Keys.DOWN)
        time.sleep(2)
        StartPlatformCode.send_keys(Keys.ENTER)
        time.sleep(2)
        StartPlatformCode.send_keys(Keys.TAB)
        time.sleep(2)
        Search = find_element_by_id_tagename_text(self,"T_scheduling-platformIndex_content-body","span","查询")
        Search.click()
        time.sleep(2)
        self.assertEqual(platformno, self.browser.find_element_by_link_text(platformno).text)#查询月台
        self.logger.info("查询月台成功......")
    except Exception as e:
        self.logger.info("查询月台失败......")
        self.logger.info(e)        
        raise RuntimeError