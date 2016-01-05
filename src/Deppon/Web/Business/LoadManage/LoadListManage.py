# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def NewLoadList(self,listtype="",arrivedpart="",plateno="",drivername="",frequencyno="",transProperty="",eirno=""):
    try:
        self.logger.info("新增配载单......")
        NewLoadList = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/em/button")   #新增配载单
        NewLoadList.click()
        time.sleep(2)
        ListType1= self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div")#配载类型
        ListType1.click()
        time.sleep(2)
        if listtype=="专线":
            ListType2=self.browser.find_element_by_xpath('''//div/ul/li[1]''')
        elif listtype=="整车":
            ListType2=self.browser.find_element_by_xpath('''//div/ul/li[2]''')
        ListType2.click()
        time.sleep(2)
        ArriveDpart = self.browser.find_element_by_name("destOrgCode")#到达部门
        ArriveDpart.send_keys(arrivedpart,Keys.ENTER)
        time.sleep(2)
        ArriveDpart.send_keys(Keys.DOWN)
        time.sleep(2)
        ArriveDpart.send_keys(Keys.ENTER)
        time.sleep(2)
        ArriveDpart.send_keys(Keys.TAB)
        time.sleep(2)
        
        sendDate1 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table[3]/tbody/tr/td[2]/table/tbody/tr/td[2]/div")#日期
        sendDate1.click()
        time.sleep(2)
        sendDate2 = self.browser.find_element_by_xpath('''//div[11]/div/div[2]/div/em/button''')#日期
        sendDate2.click()
        PlateNo = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table[5]/tbody/tr/td[2]/table/tbody/tr/td/input")#车牌号
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
        
        TransProperty1 = self.browser.find_element_by_name("transProperty")#运输性质
        TransProperty1.click()
        time.sleep(2)
        if transProperty=="精准卡航":
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.ENTER)
        elif transProperty=="精准汽运(长)":
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.DOWN)
            TransProperty1.send_keys(Keys.ENTER)
            
        time.sleep(2)
        try:
            GoodsType1 = self.browser.find_element_by_name("goodsType")#货物类型
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
        Save1 = self.browser.find_element_by_id("button-1190-btnEl")#保存
        Save1.click()
        time.sleep(2)
        #GetLoadNo = self.browser.find_element_by_id("textfield-1118-inputEl").text
        #print("LoadNo is :" + str(GetLoadNo))
        time.sleep(2)
        Save2 = self.browser.find_element_by_id("Foss_load_vehicleassemblebilladdnew_mainPage_saveButton_ID-btnInnerEl")
        Save2.click()
        Gettext = self.browser.find_element_by_id("messagebox-1001-displayfield-inputEl").text
        Gettext = Gettext.split("：")
        print(Gettext)
        self.logger.info("配载单号为："+ Gettext[1] +"......")
        return Gettext[1]
    except:
        self.logger.error("新增配载单失败......")
        raise RuntimeError
    
    