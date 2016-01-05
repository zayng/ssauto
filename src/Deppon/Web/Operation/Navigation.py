# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import xlrd
import time

def Navigation(self,str):
    '''
    操作导航栏
    '''
    self.logger.info("关闭提示......")
    try:
        self.browser.find_element_by_id("messagebox-1001").send_keys(Keys.ESCAPE)
    except:
        pass
    self.logger.info("开始操作导航栏......")
    str=str.split("-")
    '''
    for i in range(len(str)):
        time.sleep(2)
        xpath = GetXpath(self,str[i])
        oper = self.browser.find_element_by_xpath(xpath)
        oper.click()
    '''
    for i in range(len(str)):
        time.sleep(1)
        NavList = self.browser.find_element_by_id("mainNav-body").find_elements_by_tag_name("div")
        for Nav in NavList[1:]:
            if str[i]==Nav.text:
                Nav.click()
'''
def GetXpath(self,name):
    data = xlrd.open_workbook(".\\Path\\Navigation.xls")
    case = data.sheet_by_name(self.depart)
    nrows=case.nrows
    for i in range(nrows-1):
        FindXpath=case.row_values(i+1)       #取Case
        if FindXpath[0]==name:
            return (FindXpath[1])
            '''