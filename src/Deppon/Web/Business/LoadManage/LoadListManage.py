# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def NewLoadList(self,listtype="",arrivedpart="",plateno="",drivername="",frequencyno="",transProperty="",eirno=""):
    try:
        self.logger.info("�������ص�......")
        NewLoadList = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/em/button")   #�������ص�
        NewLoadList.click()
        time.sleep(2)
        ListType1= self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div")#��������
        ListType1.click()
        time.sleep(2)
        if listtype=="ר��":
            ListType2=self.browser.find_element_by_xpath('''//div/ul/li[1]''')
        elif listtype=="����":
            ListType2=self.browser.find_element_by_xpath('''//div/ul/li[2]''')
        ListType2.click()
        time.sleep(2)
        ArriveDpart = self.browser.find_element_by_name("destOrgCode")#���ﲿ��
        ArriveDpart.send_keys(arrivedpart,Keys.ENTER)
        time.sleep(2)
        ArriveDpart.send_keys(Keys.DOWN)
        time.sleep(2)
        ArriveDpart.send_keys(Keys.ENTER)
        time.sleep(2)
        ArriveDpart.send_keys(Keys.TAB)
        time.sleep(2)
        
        sendDate1 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table[3]/tbody/tr/td[2]/table/tbody/tr/td[2]/div")#����
        sendDate1.click()
        time.sleep(2)
        sendDate2 = self.browser.find_element_by_xpath('''//div[11]/div/div[2]/div/em/button''')#����
        sendDate2.click()
        PlateNo = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table[5]/tbody/tr/td[2]/table/tbody/tr/td/input")#���ƺ�
        PlateNo.send_keys(plateno,Keys.ENTER)
        time.sleep(2)
        PlateNo.send_keys(Keys.DOWN)
        time.sleep(2)
        PlateNo.send_keys(Keys.ENTER)
        time.sleep(2)
        PlateNo.send_keys(Keys.TAB)
        time.sleep(3)
        try:
            DriverName = self.browser.find_element_by_name("driverName")
            DriverName.send_keys(drivername,Keys.ENTER)
            time.sleep(2)
            DriverName.send_keys(Keys.DOWN)
            time.sleep(2)
            DriverName.send_keys(Keys.ENTER)
            time.sleep(2)
            DriverName.send_keys(Keys.TAB)
            time.sleep(3)
        except:
            pass
        if frequencyno!="":
            FrequencyNo=self.browser.find_element_by_name("frequencyNo")
            FrequencyNo.clear()
            FrequencyNo.send_keys(frequencyno)
            time.sleep(2)
        
        TransProperty1 = self.browser.find_element_by_name("transProperty")#��������
        TransProperty1.click()
        time.sleep(2)
        if transProperty=="��׼����":
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.ENTER)
        elif transProperty=="��׼����(��)":
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.ENTER)
            
        time.sleep(2)
        try:
            GoodsType1 = self.browser.find_element_by_name("goodsType")#��������
            GoodsType1.click()
            time.sleep(2)
            #GoodsType1.send_keys(Keys.DOWN)
            GoodsType1.send_keys(Keys.ENTER)
        except:
            pass

        
        AddEir1 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div[2]/div[2]/div/div/div/em/button")
        AddEir1.click()
        time.sleep(2)
        EirNo = self.browser.find_element_by_name("handOverBillNo")
        EirNo.send_keys(eirno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div[2]/div/div[2]/div/div/div/div[3]/em/button")
        Search.click()
        time.sleep(2)
        AddEir2 = self.browser.find_element_by_xpath('''//div[2]/div[2]/div/div/div/div/span''')
        AddEir2.click()
        time.sleep(2)
        Save1 = self.browser.find_element_by_id("button-1190-btnEl")#����
        Save1.click()
        time.sleep(2)
        #GetLoadNo = self.browser.find_element_by_id("textfield-1118-inputEl").text
        #print("LoadNo is :" + str(GetLoadNo))
        time.sleep(2)
        Save2 = self.browser.find_element_by_id("Foss_load_vehicleassemblebilladdnew_mainPage_saveButton_ID-btnInnerEl")
        Save2.click()
        Gettext = self.browser.find_element_by_id("messagebox-1001-displayfield-inputEl").text
        Gettext = Gettext.split("��")
        print(Gettext)
        self.logger.info("���ص���Ϊ��"+ Gettext[1] +"......")
        return Gettext[1]
    except:
        self.logger.error("�������ص�ʧ��......")
        raise RuntimeError
    
    