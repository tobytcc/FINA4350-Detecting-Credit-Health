# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:17:32 2023

@author: Toby Chiu
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import pickle

# get the textlist
with open('text-list.pickle', 'rb') as myfile:
    textList = pickle.load(myfile)
myfile.close()

# modify textList to fit parameters
for ind in range(len(textList)):
    joinedText = ' '.join(textList[ind])
    textList[ind] = joinedText

# bag of words
v = TfidfVectorizer(norm = False, smooth_idf = False)
tfidf = v.fit_transform(textList)
feature_names = v.get_feature_names_out()

# visualise tf-idf cloud
#dense = tfidf.todense()
#lst1 = dense.tolist()
#df = pd.DataFrame(lst1, columns=feature_names)
#Cloud = WordCloud(background_color="white").generate_from_frequencies(df.T.sum(axis=1))
#plt.imshow(Cloud, interpolation='bilinear')
#plt.axis("off")
#plt.show()

# finding optimal number of clusters

#wcss = []
#for i in range(1, len(textList)+1):
#    kmeans = KMeans(n_clusters = i, init='k-means++', max_iter=300, n_init = 10, random_state=0, verbose = True)
#    kmeans.fit(tfidf)
#    wcss.append(kmeans.inertia_)
    
#plt.plot(range(1, len(textList) + 1), wcss)
#plt.xlabel('cluster no.')
#plt.ylabel('wcss')
#plt.show()


# our k-means model
true_k = 3 # change as needed
model = KMeans(n_clusters = true_k, init = 'k-means++', n_init = 1)
model.fit(tfidf)

# printing top terms per cluster
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % feature_names[ind]),
    print("\n")

# To-Do: plotting our graph of clusters

# testing data
with open('testing-data.pickle', 'rb') as myfile:
    testData = pickle.load(myfile)
myfile.close()

for ind in range(len(testData)):
    joinedText = ' '.join(testData[ind])
    testData[ind] = joinedText

# making predictions
temp = v.fit_transform(testData)
prediction = model.fit_predict(temp)
print(prediction)
    