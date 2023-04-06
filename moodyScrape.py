# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:29:27 2023

@author: Toby Chiu
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time

def moodyscrape(link):

    home = os.path.expanduser('~')  # Home directory/folder.
    driver = webdriver.Chrome(service=Service(home + '/bin/chromedriver'))
    
    driver.get(link)
    
    # allow JS/Ajax to load
    driver.implicitly_wait(8)
        
    #remove login pop-up
    element = driver.find_element(By.XPATH, '//form/div/div/div/input')
    element.click()
    element.send_keys("fina4350.nlp@gmail.com") # temp email 
    element = driver.find_element(By.XPATH, '//form/div/button')
    element.click()
    driver.implicitly_wait(2)
    element = driver.find_element(By.XPATH, '//form/div/div[2]/div/input')
    element.click()
    element.send_keys("fina4350") # temp password
    element = driver.find_element(By.XPATH, '//form/div/button')
    element.click()
    
    # allow JS/Ajax to load
    time.sleep(10)
    print(driver.title)
    
    # basic scraping
    s = BeautifulSoup(driver.find_element(By.XPATH, '//main/div[2]').get_attribute('innerHTML'), 'lxml')
    raw_text = s.get_text() 
    return raw_text
    
    # UPDATE: add pre-processing here
    
    driver.close()