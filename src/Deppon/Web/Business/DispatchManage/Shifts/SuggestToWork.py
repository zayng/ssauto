# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def LoadPeopleNum(self,efficiencyperpeople):
    try:
        self.logger.info("��ʼ�����ⳡ����װ������......")
#         time.sleep(2)
#         LoadPeopleNum = find_element_by_id_tagename_text(self,"T_scheduling-adviseWorkNumberIndex_content","span","װ������")
#         LoadPeopleNum.click()
#         time.sleep(2)
        EfficiencyPerPeople = self.browser.find_element_by_name("efficiencyPerPeople")
        EfficiencyPerPeople.clear()
        EfficiencyPerPeople.send_keys(efficiencyperpeople)
        MakePeopleMsg = find_element_by_id_tagename_text(self,"T_scheduling-adviseWorkNumberIndex_content-body","span","������Ա������Ϣ")
        MakePeopleMsg.click()
        GetMsg = self.browser.find_element_by_name("message").get_attribute("value")
        self.logger.info(GetMsg)
        self.logger.info("���������ⳡ����װ������......")
        return GetMsg
    except Exception as e:
        self.logger.info("�����ⳡ����װ������ʧ��......")
        self.logger.info(e)        
        raise RuntimeError

def UnLoadPeopleNum(self,efficiencyperpeople):
    try:
        self.logger.info("��ʼ�����ⳡ����ж������......")
        LoadPeopleNum = find_element_by_id_tagename_text(self,"T_scheduling-adviseWorkNumberIndex_content","span","ж������")
        LoadPeopleNum.click()
        time.sleep(2)
        EfficiencyPerPeople = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[4]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        EfficiencyPerPeople.clear()
        EfficiencyPerPeople.send_keys(efficiencyperpeople)
        MakePeopleMsg = find_element_by_id_tagename_text(self,"T_scheduling-adviseWorkNumberIndex_content-body","span","������Ա������Ϣ")
        MakePeopleMsg.click()
        GetMsg = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[4]/div/div/table[2]/tbody/tr/td[2]/textarea").get_attribute("value")
        self.logger.info(GetMsg)
        self.logger.info("���������ⳡ����ж������......")
        return GetMsg
    except Exception as e:
        self.logger.info("�����ⳡ����ж������ʧ��......")
        self.logger.info(e)
        raise RuntimeError
    
    