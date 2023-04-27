# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:51:47 2023

@author: Toby Chiu
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import  WordNetLemmatizer

def processtext(text):
    
    # tokenization and pre-processing
    wnl = WordNetLemmatizer()
    arr = list([w for w in word_tokenize(text.lower()) if w.isalpha()])
    stemmed_arr = [wnl.lemmatize(word) for word in arr if not word in set(stopwords.words('english'))]
    print(stemmed_arr)
    
    return stemmed_arr
