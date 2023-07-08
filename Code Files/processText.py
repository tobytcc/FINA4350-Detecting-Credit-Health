# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:51:47 2023

@author: Toby Chiu
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import  WordNetLemmatizer

def processtext(text, existing_words):
    
    stemmed_arr = []
    special_words = ("moody", "moody's", "fitch", "evergrande", "scenery", "journey", "country", "garden", "sunac", \
                  "shimao", "longfor", "seazen", "cifi", "zhongliang", "zhenro", "logan", "greentown", "agile", \
                      "kwg", "ronshine", "r&f", "kaisa", "aoyuan", "fantasia", "redco", "hopson", "sinic", "jiayuan", \
                          "road", "king")
    # tokenization and pre-processing
    
    wnl = WordNetLemmatizer()
    arr = list([w for w in word_tokenize(text.lower()) if w.isalpha() \
                and len(w) > 2 and not w in set(stopwords.words('english'))])
    
    for tk in arr:
        if tk not in existing_words or tk not in special_words:
                if tk in set(words.words()):
                    stemmed_arr.append(wnl.lemmatize(tk))
                    existing_words.add(tk)
        else:
            stemmed_arr.append(wnl.lemmatize(tk))

    print(stemmed_arr, end='\n\n')
    print(existing_words)
    
    return stemmed_arr, existing_words
