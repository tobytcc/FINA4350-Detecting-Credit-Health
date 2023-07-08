# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:37:18 2023

@author: Toby Chiu
"""

import fitchScrape
import moodyScrape
import processText
import pandas as pd
import pickle

df = pd.read_csv('downgrade-reports-test.csv')

# columns to be added
rawText = [""] * (len(df))
textList = []
existing_dic = set()

for ind in df.index:
    print(ind + 1)
    ratingAgency = df['Type'][ind]
    link = df['URL'][ind]
    text = "N/A" 
    
    # scraping raw text
    if ratingAgency == "Fitch":
        text = fitchScrape.fitchscrape(link)        
    if ratingAgency == "Moody":
       text = moodyScrape.moodyscrape(link) 

    rawText[ind] = str(text)
    
    # processed list of texts
    processedText, existing_dic = processText.processtext(text, existing_dic)
    textList.append(processedText)

df.assign(domain=rawText)    

# saving data    
df.to_csv('downgrade-reports.csv')
with open('text-list.pickle', 'wb') as myfile:
    pickle.dump(textList, myfile, pickle.HIGHEST_PROTOCOL)
myfile.close()

with open('existing-dic.pickle', 'wb') as myfile:
    pickle.dump(existing_dic, myfile, pickle.HIGHEST_PROTOCOL)
myfile.close()