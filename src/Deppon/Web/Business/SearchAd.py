# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def SearchAd(self,AdCode,AdName):
    sloganCode = self.browser.find_element_by_name("sloganCode")
    sloganCode.send_keys(AdCode)
    sloganName = self.browser.find_element_by_name("sloganName")
    sloganName.send_keys(AdName)
    Search = self.browser.find_element_by_id("button-1072-btnEl")
    Search.click()