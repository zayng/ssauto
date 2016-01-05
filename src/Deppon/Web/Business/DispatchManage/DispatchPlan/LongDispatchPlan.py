# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def NewLongDispatchPlan(self,sendtime,senddepart,arrivedepart):
    try:
        self.logger.info("��ʼ������;�����ƻ�......")
        NewDispatchPlan = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/em/button")      #���������ƻ�
        NewDispatchPlan.click()
        time.sleep(2)
        SendTime = self.browser.find_element_by_xpath("//div[9]/div[2]/div/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        SendTime.clear()
        SendTime.send_keys(sendtime)
        time.sleep(2)
        SendDepart = self.browser.find_element_by_xpath("//div[2]/div/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input")#��������
        SendDepart.clear()
        SendDepart.send_keys(senddepart)
        time.sleep(2)
        SendDepart.send_keys(Keys.DOWN)
        time.sleep(2)
        SendDepart.send_keys(Keys.ENTER)
        time.sleep(2)
        SendDepart.send_keys(Keys.TAB)
        time.sleep(2)
        ArriveDepart = self.browser.find_element_by_xpath("//div[2]/div/div/div/table[3]/tbody/tr/td[2]/table/tbody/tr/td/input")#���ﲿ��
        ArriveDepart.clear()
        ArriveDepart.send_keys(arrivedepart)
        time.sleep(2)
        ArriveDepart.send_keys(Keys.DOWN)
        time.sleep(2)
        ArriveDepart.send_keys(Keys.ENTER)
        time.sleep(2)
        ArriveDepart.send_keys(Keys.TAB)
        time.sleep(2)
        Confirm = self.browser.find_element_by_xpath("//div[9]/div[2]/div/div/div/div/div/div[3]")#����
        Confirm.click()
        time.sleep(2)
        Check = self.browser.find_element_by_xpath('''//*[@id="gridview-1116"]/table/tbody/tr[2]/td[1]/div/img''')
        Check.click()
    except:
        self.logger.error("������;�����ƻ�ʧ��......")
        raise RuntimeError

def MakeLongDispatchPlanInCar(self,caravan,plateno,plantime,usestarttime,useendtime,addplateno,adddriver):
    time.sleep(2)
    try:
        AddCar = self.browser.find_element_by_xpath("//div[3]/div[2]/div/div/div/em/button")#�ӷ���˾��
        AddCar.click()
    except:
        pass
    time.sleep(2)
    try:
        AddCar = self.browser.find_element_by_id("button-1291-btnInnerEl")#�ӷ���˾��
        AddCar.click()
    except:
        pass
    time.sleep(2)
    try:
        ConfirmCar = self.browser.find_element_by_id("button-1005-btnInnerEl")
        ConfirmCar.click()
    except:
        pass
    #button-1005-btnInnerEl
    time.sleep(2)
    addcaravan= self.browser.find_element_by_name("vo.carDto.carOwnerCode") #���ӳ���
    addcaravan.send_keys(caravan)
    time.sleep(2)
    addcaravan.send_keys(Keys.DOWN)
    time.sleep(2)
    addcaravan.send_keys(Keys.ENTER)
    time.sleep(2)
    addcaravan.send_keys(Keys.TAB)
    time.sleep(2)

    plateNo= self.browser.find_element_by_name("vo.carDto.vehicleNo") #���ӳ���
    plateNo.send_keys(plateno)
    time.sleep(2)
    plateNo.send_keys(Keys.DOWN)
    time.sleep(2)
    plateNo.send_keys(Keys.ENTER)
    time.sleep(2)
    plateNo.send_keys(Keys.TAB)
    time.sleep(2)
    Search = self.browser.find_element_by_xpath("//div[2]/div/div[2]/div/div/div/div[3]/em/button")#��ѯ
    Search.click()
    time.sleep(2)
    GetCar= self.browser.find_element_by_xpath('''//div[3]/div/table/tbody/tr[2]/td/div/div''')  #ѡ��
    GetCar.click()
    time.sleep(2)
    PlanTime = self.browser.find_element_by_id("innerplanDepartTime-inputEl")#�ƻ�����ʱ��
    PlanTime.clear()
    PlanTime.send_keys(plantime)
    time.sleep(2)
    UseStartTime = self.browser.find_element_by_id("platformTimeStart-date97-1_first-inputEl")#ʹ�ÿ�ʼʱ��
    UseStartTime.clear()
    UseStartTime.send_keys(usestarttime)
    time.sleep(2)
    UseEndTime = self.browser.find_element_by_id("platformTimeStart-date97-1_second-inputEl")#ʹ�ý���ʱ��
    UseEndTime.clear()
    UseEndTime.send_keys(useendtime)
    AddPlateNo = self.browser.find_element_by_name("longCarGroup")#���ӳ���
    AddPlateNo.send_keys(addplateno)
    time.sleep(2)
    AddPlateNo.send_keys(Keys.DOWN)
    time.sleep(2)
    AddPlateNo.send_keys(Keys.ENTER)
    time.sleep(2)
    AddPlateNo.send_keys(Keys.TAB)
    time.sleep(2)
    AddDriver = self.browser.find_element_by_name("driverCode1")#����˾��
    AddDriver.clear()
    AddDriver.send_keys(adddriver)
    time.sleep(2)
    AddDriver.send_keys(Keys.DOWN)
    time.sleep(2)
    AddDriver.send_keys(Keys.ENTER)
    time.sleep(2)
    AddDriver.send_keys(Keys.TAB)
    time.sleep(2)
    Save = self.browser.find_element_by_xpath("//div[2]/div[3]/div/div/div/div[3]/em/button")#����
    Save.click()
    time.sleep(2)
    Close = self.browser.find_element_by_xpath("//div[2]/div[3]/div/div/div/div/em/button")#�ر�
    Close.click()
    time.sleep(2)
    Sort = self.browser.find_element_by_xpath("//div[3]/div[3]/div/div/div[4]/div/span")
    Sort.click()
    time.sleep(2)
    Sort.click()
    time.sleep(2)
    Select = self.browser.find_element_by_xpath('''//tr[2]/td/div/div''')#����
    Select.click()
    time.sleep(2)
    Issued = self.browser.find_element_by_xpath("//div[3]/div[2]/div/div/div[3]/em/button")#�·�
    Issued.click()
    try:
        Confirm = self.browser.find_element_by_id("button-1005-btnEl")
        Confirm.click()
    except:
        pass
    try:
        Confirm = self.browser.find_element_by_id("button-1006-btnEl")
        Confirm.click()
    except:
        pass
    time.sleep(2)
    pass