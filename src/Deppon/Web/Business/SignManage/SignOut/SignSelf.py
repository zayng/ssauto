# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def SignSelf(self,billno):
    try:
        self.logger.info("��ʼ�ͻ�����ǩ��......")
        Billno = self.browser.find_element_by_name("waybillNo")      #�˵���
        Billno.send_keys(billno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div[3]/em/button")      #��ѯ
        Search.click()
        time.sleep(2)
        Sign = self.browser.find_element_by_xpath('''//div[2]/div[3]/div/table/tbody/tr[2]/td/div/img''')       #ǩ��
        Sign.click()
        time.sleep(2)
        SignThing = self.browser.find_element_by_xpath("//div[2]/div[2]/div[2]/div/div/div/div/span")#ȫѡ����
        SignThing.click()
        time.sleep(2)
        try:
            Confirm1 = self.browser.find_element_by_id("button-1104-btnEl")#ȷ��
            Confirm1.click()
        except:
            pass
        try:
            Confirm2 = self.browser.find_element_by_id("button-1105-btnEl")#ȷ��
            Confirm2.click()
        except:
            pass
        time.sleep(2)
        Confirm2 = self.browser.find_element_by_id("button-1006-btnInnerEl")#ȷ��
        Confirm2.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "ǩ�ճ���ɹ��������˶��ţ��ջ��˶��ţ�����֪ͨ�����ͳɹ���":
            self.logger.info(reslut)
            self.logger.info("��������ǩ��......")
        else:
            raise RuntimeError
    except:
        self.logger.error("����ǩ��ʧ��......")
        raise RuntimeError
    