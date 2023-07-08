# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:33:55 2023

@author: Toby Chiu
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os

def fitchscrape(link):

    home = os.path.expanduser('~')  # Home directory/folder.
    driver = webdriver.Chrome(service=Service(home + '/bin/chromedriver'))
    
    driver.get(link)
    
    # allow JS/Ajax to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "RAC")))
    print(driver.title)
    
    # basic scraping
    s = BeautifulSoup(driver.find_element(By.CLASS_NAME, "RAC").get_attribute('innerHTML'), 'lxml') 
    raw_text = s.get_text()
    
    # pre-processing 
    processed_text = raw_text.split("Best/Worst Case Rating Scenario")    
    return processed_text[0]

    driver.close()

