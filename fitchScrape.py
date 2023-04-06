# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:33:55 2023

@author: Toby Chiu
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time

def fitchscrape(link):

    home = os.path.expanduser('~')  # Home directory/folder.
    driver = webdriver.Chrome(service=Service(home + '/bin/chromedriver'))
    
    driver.get(link)
    
    # allow JS/Ajax to load
    time.sleep(5)
    print(driver.title)
    
    # basic scraping
    s = BeautifulSoup(driver.find_element(By.CLASS_NAME, "RAC").get_attribute('innerHTML'), 'lxml') 
    raw_text = s.get_text()
    return raw_text
    
# UPDATE: add pre-processing here
    
    driver.close()

