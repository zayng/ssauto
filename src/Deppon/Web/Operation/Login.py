# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def Login(self,url,username,passwd,depart=""):
    '''
    ��½
    '''
    self.logger.info("��ʼ��½......")
    self.browser.get(url)
    LoginName = self.browser.find_element_by_name("loginName")
    LoginName.send_keys(username)
    password = self.browser.find_element_by_name("password")
    password.send_keys(passwd)
    password.send_keys(Keys.RETURN)
    self.depart=depart