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

df = pd.read_csv('downgrade-reports.csv')

# columns to be added
rawText = [""] * (len(df))
textList = []

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
    df.assign(domain=rawText)
    
    # processed list of texts
    processedText = processText.processtext(text)
    textList.append(processedText)
    
    # BoW
    # bowText = bagOfWords.bagofwords(text) 
    # bow[ind] = bowText
    # df.assign(domain=bow)
  
# saving data    
df.to_csv('downgrade-reports.csv')
with open('text-list.pickle', 'wb') as myfile:
    pickle.dump(textList, myfile, pickle.HIGHEST_PROTOCOL)
myfile.close()