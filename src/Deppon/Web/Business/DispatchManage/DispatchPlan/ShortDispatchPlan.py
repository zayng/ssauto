# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def NewShortDispatchPlan(self,sendtime,senddepart,arrivedepart):
    self.logger.info("开始新增短途发车计划......")
    NewDispatchPlan = self.browser.find_element_by_id("button-1119-btnEl")      #新增发车计划
    NewDispatchPlan.click()
    time.sleep(2)
    SendTime = self.browser.find_element_by_id("datefield-1066-inputEl")
    SendTime.clear()
    SendTime.send_keys(sendtime)
    time.sleep(2)
    SendDepart = self.browser.find_element_by_id("dynamicorgcombselector-1067-inputEl")#出发部门
    SendDepart.clear()
    SendDepart.send_keys(senddepart)
    time.sleep(2)
    SendDepart.send_keys(Keys.DOWN)
    time.sleep(2)
    SendDepart.send_keys(Keys.ENTER)
    time.sleep(2)
    SendDepart.send_keys(Keys.TAB)
    time.sleep(2)
    ArriveDepart = self.browser.find_element_by_id("dynamicorgcombselector-1068-inputEl")#到达部门
    ArriveDepart.clear()
    ArriveDepart.send_keys(arrivedepart)
    time.sleep(2)
    ArriveDepart.send_keys(Keys.DOWN)
    time.sleep(2)
    ArriveDepart.send_keys(Keys.ENTER)
    time.sleep(2)
    ArriveDepart.send_keys(Keys.TAB)
    time.sleep(2)
    Confirm = self.browser.find_element_by_id("button-1072-btnEl")#新增
    Confirm.click()
    time.sleep(2)
    Check = self.browser.find_element_by_xpath('''//*[@id="gridview-1117"]/table/tbody/tr[2]/td[1]/div/img''')
    Check.click()
    pass
def MakeShortDispatchPlanInCar(self,caravan,plateno,addplateno,adddriver):
    time.sleep(2)
    AddCar = self.browser.find_element_by_id("button-1288-btnInnerEl")#加发公司车
    AddCar.click()
    time.sleep(2)
    addcaravan= self.browser.find_element_by_id("commonmotorcadeselector-1179-inputEl")
    addcaravan.send_keys(caravan)
    time.sleep(2)
    addcaravan.send_keys(Keys.DOWN)
    time.sleep(2)
    addcaravan.send_keys(Keys.ENTER)
    time.sleep(2)
    addcaravan.send_keys(Keys.TAB)
    time.sleep(2)

    plateNo= self.browser.find_element_by_id("commonowntruckselector-1182-inputEl")
    plateNo.send_keys(plateno)
    time.sleep(2)
    plateNo.send_keys(Keys.DOWN)
    time.sleep(2)
    plateNo.send_keys(Keys.ENTER)
    time.sleep(2)
    plateNo.send_keys(Keys.TAB)
    time.sleep(2)
    Search = self.browser.find_element_by_id("button-1186-btnInnerEl")
    Search.click()
    time.sleep(2)
    GetCar= self.browser.find_element_by_xpath('''//*[@id="gridview-1199"]/table/tbody/tr[2]/td[1]/div/div''')
    GetCar.click()
    time.sleep(2)
    AddPlateNo = self.browser.find_element_by_id("commonmotorcadeselector-1207-inputEl")
    AddPlateNo.send_keys(addplateno)
    time.sleep(2)
    AddPlateNo.send_keys(Keys.DOWN)
    time.sleep(2)
    AddPlateNo.send_keys(Keys.ENTER)
    time.sleep(2)
    AddPlateNo.send_keys(Keys.TAB)
    time.sleep(2)
    AddDriver = self.browser.find_element_by_id("commonowndriverselector-1212-inputEl")#增加司机
    AddDriver.clear()
    AddDriver.send_keys(adddriver)
    time.sleep(2)
    AddDriver.send_keys(Keys.DOWN)
    time.sleep(2)
    AddDriver.send_keys(Keys.ENTER)
    time.sleep(2)
    AddDriver.send_keys(Keys.TAB)
    time.sleep(2)
    Save = self.browser.find_element_by_id("button-1233-btnEl")
    Save.click()
    time.sleep(2)
    Confirm = self.browser.find_element_by_id("button-1006-btnInnerEl")
    Confirm.click()
    pass
def MakeShortDispatchPlanOutCar(self,t):
    pass
