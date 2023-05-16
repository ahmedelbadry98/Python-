##########################################################################################
#                 important Includes for selenium and beautifulsoup                      #
##########################################################################################
import bs4
import random
from lxml import etree
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from PIL import Image
from selenium import webdriver
from PyQt5.QtGui import QTextCursor
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import sys
import os
import re
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from PIL import Image
from selenium import webdriver
from PyQt5.QtGui import QTextCursor
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.alert import Alert
import numpy as np
from tabulate import tabulate
import datetime
import winsound
import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import re, itertools
from selenium import webdriver
from bs4 import BeautifulSoup as BS



##########################################################################################
#                              Functions                                                 #
##########################################################################################
def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


def click_x_path(xpath):
    varr = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    varr.click()


def data_to_x_path(xpath, data):
    varr = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    varr.send_keys(data)


def get_attribute_value(object,attribute_value):
    attribute = object.attrs
    print("All div attributes:", attribute)
    return attribute[attribute_value]


##########################################################################################
#                              Edge options                                              #
##########################################################################################
try:
    try:
        driver = webdriver.Edge(executable_path="Edge.exe")
    except:
        print("install driver")
        driver = Edge(executable_path=EdgeChromiumDriverManager().install())
except Exception as E:
    print(E)
    quit()



##########################################################################################
#                            open calendar website                                       #
##########################################################################################

driver.get('https://outlook.office.com/calendar/view/month')
driver.maximize_window()
time.sleep(3)

##########################################################################################
#                   save html code into a variable                                       #
##########################################################################################

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

##########################################################################################
#       search for the element 'button or input text-area ... etc' with a                #
#       unique identifier such as class or any other attribute                           #
##########################################################################################
x = soup.find_all("input", {"type": "email"})


##########################################################################################
#       print the returned list length to make sure that it contain only one element     #
##########################################################################################
print(len(x))
print("--------------------------------------")


##########################################################################################
#                           print element x-path                                         #
##########################################################################################
web_elemnt = x[0]
print(xpath_soup(web_elemnt))








