# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time
import traceback

def AddEir(self,handovertype="",reachDepart="",truckNum="",driver="",waybill="",loadendtime=""):
    '''
    �������ӵ�
    '''
    try:
        self.logger.info("��ʼ�����������ӵ�......")
        #print(self.browser.get_text(self.browser.find_element_by_name("handOverBillNo")))
        NewEir = self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/em/button")
        NewEir.click()
        time.sleep(5)
        try:
            handOverType=self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div")
            handOverType.click()
            time.sleep(5)
            if handovertype=="���佻�ӵ�":
                handOverType = self.browser.find_element_by_xpath('''//li[1]''')
                handOverType.click()
            elif handovertype=="���佻�ӵ�":
                handOverType = self.browser.find_element_by_xpath('''//li[2]''')
                handOverType.click()
            elif handovertype=="�ⷢ���ӵ�":
                handOverType = self.browser.find_element_by_xpath('''//li[3]''')
                handOverType.click()
            else:
                pass
        except:
            print(handovertype)
            traceback.print_exc()
            pass
        time.sleep(2)
        if handovertype == "���佻�ӵ�" or handovertype=="���佻�ӵ�":
            ReachDepart = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table[5]/tbody/tr/td[2]/table/tbody/tr/td/input")   #���ﲿ��
        elif handovertype == "�ⷢ���ӵ�":
            ReachDepart = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/table[6]/tbody/tr/td[2]/table/tbody/tr/td/input")   #���ﲿ��
        ReachDepart.send_keys(reachDepart,Keys.ENTER)
        time.sleep(2)
        ReachDepart.send_keys(Keys.DOWN)
        time.sleep(2)
        ReachDepart.send_keys(Keys.ENTER)
        time.sleep(2)
        ReachDepart.send_keys(Keys.TAB)
        TruckNum = self.browser.find_element_by_xpath("//table[7]/tbody/tr/td[2]/table/tbody/tr/td/input")      #���ƺ�
        TruckNum.send_keys(truckNum,Keys.ENTER)
        time.sleep(2)
        TruckNum.send_keys(Keys.DOWN)
        time.sleep(2)
        TruckNum.send_keys(Keys.ENTER)
        time.sleep(2)
        TruckNum.send_keys(Keys.TAB)
        time.sleep(2)
        Driver = self.browser.find_element_by_name("driver") #˾��
        Driver.clear()
        Driver.send_keys(driver,Keys.ENTER)
        time.sleep(2)
        Driver.send_keys(Keys.DOWN)
        time.sleep(2)
        Driver.send_keys(Keys.ENTER)
        time.sleep(2)
        Driver.send_keys(Keys.TAB)
        Bill=self.browser.find_element_by_xpath("//table[15]/tbody/tr/td[2]/input") #�Ƿ�Ԥ�佻�ӵ�
        Bill.click()
        time.sleep(2)
        LoadEndTime=self.browser.find_element_by_id("Foss_handOverBillAddNew_loadEndTime_ID-inputEl") #���ʱ��
        LoadEndTime.send_keys(loadendtime)
        time.sleep(2)
        try:
            if handovertype=="���佻�ӵ�":
                GoodsType1 = self.browser.find_element_by_name("goodsType")#��������
                GoodsType1.click()
                time.sleep(2)
                #GoodsType1.send_keys(Keys.DOWN)
                GoodsType1.send_keys(Keys.ENTER)
                #GoodsType2 = self.browser.find_element_by_xpath('''//div[23]/div/ul/li''')#��������
                #GoodsType2.click()
        except:
            pass
        Waybill = self.browser.find_element_by_name("Foss_load_handOverBillAddnew_quickAddWaybillNo_ID-inputEl")#�˵���
        Waybill.send_keys(waybill)
        time.sleep(2)
        #if finishTime!="": 
        #    FinishTime=self.browser.find_element_by_id("Foss_handOverBillAddNew_loadEndTime_ID-inputEl")
        #    FinishTime.send_keys(finishTime)
        QuickAdd = self.browser.find_element_by_id("Foss_load_handOverBillAddnew_quickAddButton_ID-btnEl")#�������
        QuickAdd.click()
        time.sleep(15)
        Save = self.browser.find_element_by_id("Foss_load_handoverbilladdnew_mainPage_saveButton_ID-btnInnerEl")#����
        Save.click()
        time.sleep(2)
        
        GetHandOverBillNo = self.browser.find_element_by_xpath("//div[2]/table/tbody/tr/td[2]/div").text
        GetHandOverBillNo = GetHandOverBillNo.split("��")
        Confirm = self.browser.find_element_by_id("button-1005-btnEl")
        Confirm.click()
        self.logger.info("���ɽ��ӵ��ɹ������ӵ���Ϊ: "+ GetHandOverBillNo[1] +"......")
        return GetHandOverBillNo[1]
    except:
        self.logger.info("���ɽ��ӵ�ʧ��......")
        raise RuntimeError
    