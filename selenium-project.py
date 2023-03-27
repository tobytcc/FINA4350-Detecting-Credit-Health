# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:33:55 2023

@author: Toby Chiu
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time

home = os.path.expanduser('~')  # Home directory/folder.
driver = webdriver.Chrome(service=Service(home + '/bin/chromedriver'))

# UPDATE: can turn into automatic input with csv file
driver.get('https://www.fitchratings.com/research/corporate-finance/fitch-downgrades-evergrande-subsidiaries-hengda-tianji-to-restricted-default-09-12-2021')

# allow JS/Ajax to load
time.sleep(5)

#filename
title = driver.title.replace(' ', '-') + '.html'

# basic scraping
with open(title, 'w' , encoding='utf-8') as f:
    f.write(driver.page_source)
    s = BeautifulSoup(driver.page_source, 'lxml')
    #print(s.prettify())
    raw_text = s.get_text()
    print(raw_text)
    
# UPDATE: add pre-processing here

# UPDATE: add BoW here
    
    
driver.close()

