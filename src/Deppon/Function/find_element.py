# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time

def find_element_by_id_tagename_text(self,id,tagname,texts):
    elements = self.browser.find_element_by_id(id).find_elements_by_tag_name(tagname)
    for element in elements[1:]:
        #print(element.text)
        if element.text == texts:
           
            return element
def find_element_by_id_tagename(self,id,tagname):
    element = self.browser.find_element_by_id(id).find_element_by_tag_name(tagname)
    return element