# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:17:32 2023

@author: Toby Chiu
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
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
dense = tfidf.todense()
lst1 = dense.tolist()
df = pd.DataFrame(lst1, columns=feature_names)
Cloud = WordCloud(background_color="white").generate_from_frequencies(df.T.sum(axis=1))
plt.imshow(Cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

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
true_k = 5 # change as needed
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

# reducing to 2 features (dimensions) for plotting
tfidf_array = normalize(tfidf).toarray()
pca = PCA(n_components = 2)
Y_sklearn = pca.fit_transform(tfidf_array)
fitted = model.fit(Y_sklearn)
predicted_values = model.fit_predict(Y_sklearn)

# plotting our graph of clusters
plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], c=predicted_values, s=50, cmap='viridis')
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

# testing data
with open('5-2_testingdata_v1.pickle', 'rb') as myfile:
    testData = pickle.load(myfile)
myfile.close()

# making predictions
temp = v.fit_transform(testData)
prediction = model.fit_predict(temp)
print(prediction)

    
    