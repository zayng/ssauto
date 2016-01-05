# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from Deppon.Function.find_element import *
import time

def AskOutCarAppoint(self,usepurpose,usetype,cartype,dispatchtransdept,arrivedeptode,useaddress,weight,goodspackege,goodsqty,volume,clientname,clientcontactphone):
    try:
        self.logger.info("开始约车申请......")
        NewDispatchPlan = self.browser.find_element_by_id("Foss.scheduling.inviteVehicle.InviteVehicleApplyQueryGrid.toolbar.button.apply.id-btnInnerEl")      #申请外请车
        NewDispatchPlan.click()
        time.sleep(2)
        UsePurpose = self.browser.find_element_by_xpath("//fieldset/div/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        UsePurpose.click()
        if usepurpose == "外请车约车":
            self.browser.find_element_by_xpath("//div/ul/li").click()
        elif usepurpose == "整车约车":
            self.browser.find_element_by_xpath("//li[2]").click()
        UseType = self.browser.find_element_by_xpath("//fieldset/div/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td/input")
        UseType.click()
        time.sleep(2)
        if usetype == "到营业部":
            #UseType.send_keys(Keys.DOWN)
            UseType.send_keys(Keys.ENTER)
            #self.browser.find_element_by_xpath("//div[15]/div/ul/li").click()
        elif usetype == "到客户处":
            UseType.send_keys(Keys.DOWN)
            UseType.send_keys(Keys.ENTER)
            #self.browser.find_element_by_xpath("//div[15]/div/ul/li[2]").click()
        elif usetype == "到中转场":
            UseType.send_keys(Keys.DOWN)
            UseType.send_keys(Keys.ENTER)
            #self.browser.find_element_by_xpath("//li[3]").click()
        
        CarType = self.browser.find_element_by_xpath("//table[3]/tbody/tr/td[2]/table/tbody/tr/td/input")
        CarType.send_keys(cartype,Keys.ENTER)
        time.sleep(2)
        CarType.send_keys(Keys.DOWN)
        time.sleep(2)
        CarType.send_keys(Keys.ENTER)
        time.sleep(2)
        CarType.send_keys(Keys.TAB)
        
        self.browser.find_element_by_xpath("//fieldset/div/div/div/table[5]/tbody/tr/td[2]/table/tbody/tr/td[2]/div").click()
        clock = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to_frame(clock)
        date = self.browser.find_element_by_xpath("//td[@onclick='day_Click(2013,6,29);']")
        date.click()
        Confirm1 = self.browser.find_element_by_xpath("//input[@id='dpOkInput']")
        Confirm1.click()
        self.browser.switch_to_default_content()
        
        DispatchTransDept = self.browser.find_element_by_name("dispatchTransDept")
        DispatchTransDept.send_keys(dispatchtransdept,Keys.ENTER)
        time.sleep(2)
        DispatchTransDept.send_keys(Keys.DOWN)
        time.sleep(2)
        DispatchTransDept.send_keys(Keys.ENTER)
        time.sleep(2)
        DispatchTransDept.send_keys(Keys.TAB)
        '''
    
        ApplyEmpCode = self.browser.find_element_by_name("applyEmpCode")
        ApplyEmpCode.send_keys(applyempcode,Keys.ENTER)
        time.sleep(2)
        ApplyEmpCode.send_keys(Keys.DOWN)
        time.sleep(2)
        ApplyEmpCode.send_keys(Keys.ENTER)
        time.sleep(2)
        ApplyEmpCode.send_keys(Keys.TAB)
        
        '''
        if usepurpose == "整车约车":
            ArriveDepart = self.browser.find_element_by_name("arrivedDeptCode")
            ArriveDepart.send_keys(arrivedeptode,Keys.ENTER)
            time.sleep(2)
            ArriveDepart.send_keys(Keys.DOWN)
            time.sleep(2)
            ArriveDepart.send_keys(Keys.ENTER)
            time.sleep(2)
            ArriveDepart.send_keys(Keys.TAB)
        UseAddress = self.browser.find_element_by_name("useAddress")
        UseAddress.send_keys(useaddress)
        
        if usepurpose == "整车约车":
            Weight = self.browser.find_element_by_name("weight")
            Weight.send_keys(weight)
            GoodsPackege = self.browser.find_element_by_name("goodsPackege")
            GoodsPackege.send_keys(goodspackege)
            GoodsQty = self.browser.find_element_by_name("goodsQty")
            GoodsQty.send_keys(goodsqty)
            Volume = self.browser.find_element_by_name("volume")
            Volume.send_keys(volume)
            ClientName = self.browser.find_element_by_name("clientName")
            ClientName.send_keys(clientname)
            ClientContactPhone = self.browser.find_element_by_name("clientContactPhone")
            ClientContactPhone.send_keys(clientcontactphone)
            
            
            
                    
        Confirm2 = self.browser.find_element_by_xpath("//div[2]/div/div/div/div/div[2]/em/button")
        Confirm2.click()
        time.sleep(2)
        GetCode = self.browser.find_element_by_id("messagebox-1001-displayfield-inputEl").text
        GetCode = GetCode.split("：")
        time.sleep(2)
        Confirm3 = self.browser.find_element_by_id("button-1005-btnInnerEl")
        Confirm3.click()
        self.logger.info("申请约车，申请单号为: "+ GetCode[1] +"......")
        return GetCode[1]
    except:
        self.logger.error("约车申请失败......")
        raise RuntimeError
def DealAskOutCarAppoint(self,inviteno,carno,invitecost):
    try:
        self.logger.info("开始审核外请车......")
        InviteNo = self.browser.find_element_by_name("inviteNo")
        InviteNo.send_keys(inviteno)
        
        Search = self.browser.find_element_by_xpath("//div/div[2]/div/div/div/div[3]/em/button")
        Search.click()
        time.sleep(2)
        SelectAll1 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/span")
        SelectAll1.click()
        Deal = self.browser.find_element_by_id("Foss.scheduling.inviteVehicle.InviteVehicleApplyQueryGrid.toolbar.button.audit.id-btnInnerEl")
        Deal.click()
        time.sleep(2)
        SelectAll2 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/span")
        SelectAll2.click()
        
        CarNo = self.browser.find_element_by_xpath("//div[2]/div/div/div/table/tbody/tr/td[2]/table/tbody/tr/td/input")
        CarNo.send_keys(carno,Keys.ENTER)
        time.sleep(2)
        CarNo.send_keys(Keys.DOWN)
        time.sleep(2)
        CarNo.send_keys(Keys.ENTER)
        time.sleep(2)
        CarNo.send_keys(Keys.TAB)
        time.sleep(2)
        Search = find_element_by_id_tagename_text(self,"T_scheduling-passInviteVehicleIndex_content-body","span","查询")
        Search.click()
        time.sleep(2)
        SelectAll3 =self.browser.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/span")
        SelectAll3.click()
        InviteCost = self.browser.find_element_by_name("inviteCost")
        InviteCost.send_keys(invitecost)
        ArriveTime = self.browser.find_element_by_xpath("//div[3]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/div")
        ArriveTime.click()
        
        clock = self.browser.find_element_by_tag_name("iframe")
        self.browser.switch_to_frame(clock)
        date = self.browser.find_element_by_id("dpTodayInput")
        date.click()
        '''Confirm1 = self.browser.find_element_by_xpath("//input[@id='dpOkInput']")
        Confirm1.click()'''
        self.browser.switch_to_default_content()
        
        Accept = find_element_by_id_tagename_text(self,"T_scheduling-passInviteVehicleIndex_content-body","span","通过")
        Accept.click()
        self.logger.info("审核外请车成功......")
    except:
        self.logger.error("审核外请车失败......")
        raise RuntimeError
def CheckInOutCar(self,inviteno,):
    try:
        self.logger.info("开始进行外请车报到......")
        InviteNo = self.browser.find_element_by_name("inviteNo")
        InviteNo.send_keys(inviteno)
        time.sleep(2)
        Search = self.browser.find_element_by_xpath("//div/div[2]/div/div/div/div[3]/em/button")
        Search.click()
        time.sleep(2)
        SelectAll1 = self.browser.find_element_by_xpath("//div[3]/div/div/div/div/span")
        SelectAll1.click()
        time.sleep(2)
        CheckIn = self.browser.find_element_by_id("Foss.scheduling.inviteVehicle.InviteVehicleApplyQueryGrid.toolbar.button.arrive.id-btnInnerEl")
        CheckIn.click()
        time.sleep(2)
        Confirm1 = self.browser.find_element_by_id("button-1123-btnInnerEl")
        Confirm1.click()
        time.sleep(2)
        Confirm2 = self.browser.find_element_by_id("button-1006-btnInnerEl")
        Confirm2.click()
        self.logger.info("外请车报到成功......")
    except:
        self.logger.error("外请车报到失败......")
        raise RuntimeError

