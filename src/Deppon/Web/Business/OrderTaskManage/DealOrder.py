# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def SearchOrder(self,orderno):
    try:
        self.logger.info("��ʼ��ѯ����......")
        OrderNo = self.browser.find_element_by_name("orderNo")
        OrderNo.send_keys(orderno)
        Search = find_element_by_id_tagename_text(self,"Foss_order_orderHandle_orderHandleQueryForm_Id-innerCt","span","��ѯ")
        Search.click()
        time.sleep(2)
        self.assertRegexpMatches(self.browser.find_element_by_css_selector("BODY").text, r"^[\s\S]*%s[\s\S]*$" % orderno)
        GetOrder = self.browser.find_element_by_css_selector("div.x-grid-row-checker")
        GetOrder.click()
        self.logger.info("��ѯ�����ɹ�......")
        #time.sleep(5)
        #print(self.browser.find_element_by_css_selector("BODY").text, r"^[\s\S]*Y3686[\s\S]*$")
    except Exception as e:
        self.logger.error("��ѯ����ʧ��......")
        self.logger.error(e)
        raise RuntimeError

def ReturnOrder(self,orderno,reason):
    try:
        SearchOrder(self,orderno)
        self.logger.info("��ʼ�˻ض���......")
        ReturnOrder = self.browser.find_element_by_xpath("//td[3]/div/img")  #�˻ض���
        ReturnOrder.click()
        if reason=="��ַ����":
            Reason = self.browser.find_element_by_xpath("//td/table/tbody/tr/td[2]/input")#�˻�ԭ��
            Reason.click()
        else:
            Reason = self.browser.find_element_by_xpath("//td[2]/table/tbody/tr/td[2]/input")
            Reason.click()
            Desc = self.browser.find_element_by_name("desc")
            Desc.send_keys(reason)
        Confirm = self.browser.find_element_by_xpath("//div[2]/div/div/div[2]/div/div/div/em/button")#ȷ��
        Confirm.click()
        try:
            Confirm1 =  ("button-1005-btnInnerEl")
            Confirm1.click()
        except:
            pass
        self.logger.info("�˻ض����ɹ�......")
    except Exception as e:
        self.logger.error("�˻ض���ʧ��......")
        self.logger.error(e)
        raise RuntimeError
def DealOrder(self,orderno,vehicleno):
    try:
        SearchOrder(self,orderno)
        #OuterCar = 
        SearchCar = find_element_by_id_tagename_text(self,"T_order-orderHandleIndex_content-body","span","��ѯ����")    #�����ѯ����
        SearchCar.click()
        time.sleep(1)
        OuterCar = find_element_by_id_tagename_text(self,"T_order-orderHandleIndex_content-body","span","���복")    #������복
        OuterCar.click()
        VehicleNo = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        VehicleNo.send_keys(vehicleno,Keys.ENTER)
        time.sleep(2)
        VehicleNo.send_keys(Keys.DOWN)
        time.sleep(2)
        VehicleNo.send_keys(Keys.ENTER)
        time.sleep(2)
        VehicleNo.send_keys(Keys.TAB)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[2]/div[2]/div/div/div[3]/em/button")    
        Search.click()  #�����ѯ
        GetCar = self.browser.find_element_by_css_selector("div.x-grid-row-radio")#ѡ��
        GetCar.click()
        Deal = find_element_by_id_tagename_text(self,"T_order-orderHandleIndex_content-body","span","����")    #�����ѯ����
        Deal.click()
        reslut = find_element_by_id_tagename(self,"msg-div","p").text
        if reslut == "����ɹ�":
            self.logger.info(reslut)
            self.logger.info("�������ɹ�......")
        else:
            self.logger.error(reslut)
            raise RuntimeError
    except Exception as e:
        self.logger.error("������ʧ��......")
        self.logger.error(e)
        raise RuntimeError