# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def Login(self,url,username,passwd,depart=""):
    '''
    登陆
    '''
    self.logger.info("开始登陆......")
    self.browser.get(url)
    LoginName = self.browser.find_element_by_name("loginName")
    LoginName.send_keys(username)
    password = self.browser.find_element_by_name("password")
    password.send_keys(passwd)
    password.send_keys(Keys.RETURN)
    self.depart=depart