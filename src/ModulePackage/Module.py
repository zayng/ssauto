import unittest
import time
import datetime
import os
import traceback
import logging.config
import logging
import sys

sys.path.append("C:\workspace\FossAutoTest")
sys.path.append("C:\Python33")
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from Deppon.Web.Operation.Login import *
from Deppon.Web.Business.LoadManage.LoadSeal import *
from Deppon.Web.Business.LoadManage.EirManage import *
from Deppon.Web.Business.LoadManage.LoadListManage import *
from Deppon.Web.Operation.Navigation import *
from Deppon.Web.Business.TruckManage.ConfirmSA import *
from Deppon.Web.Business.UnloadManage.ConfirmUnloadTask import *
from Deppon.Web.Business.UnloadManage.NewUnloadTask import *
from Deppon.Web.Business.DispatchManage.DispatchPlan.ShortDispatchPlan import *
from Deppon.Web.Business.DispatchManage.DispatchPlan.LongDispatchPlan import *
from Deppon.Web.Business.SendManage.NotifyCustomer import *
from Deppon.Web.Business.SignManage.SignOut.SignSelf import *
from Deppon.Web.Business.SignManage.SettlementGoods import *
from Deppon.Web.Business.OutgoingManage.AirManage.NewAirlinesBill import *
from Deppon.Web.Business.OutgoingManage.AirManage.NewAirlineEir import *
from Deppon.Web.Business.AppointCarManage.OutCarAppoint import *
from Deppon.Web.Business.OutgoingManage.FarOffLineManage.SearchFarOffWaybill import *
from Deppon.Web.Business.SignManage.AirFarOffSign import *
from Deppon.Web.Business.OrderTaskManage.DealOrder import *
from Deppon.Web.Business.DispatchManage.Shifts.SuggestToWork import *
from Deppon.Web.Business.DispatchManage.DispatchPlatform import *
#from xlutils.copyd import copyd
from xlrd import open_workbook

