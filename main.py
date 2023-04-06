# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:37:18 2023

@author: Toby Chiu
"""

import fitchScrape
import moodyScrape
import pandas as pd

df = pd.read_csv('downgrade-reports.csv')

# columns to be added
rawText = []

for ind in df.index:
    print(ind + 1)
    ratingAgency = df['Type'][ind]
    link = df['URL'][ind]
    text = "N/A" 
    
    # scraping raw text
    if ratingAgency == "Fitch":
        text = fitchScrape.fitchscrape(link)        
    elif ratingAgency == "Moody":
        text = moodyScrape.moodyscrape(link) 

    rawText.append(str(text))

df['RawText'] = rawText

# UPDATE: add BoW here

df.to_csv('downgrade-reports.csv')
