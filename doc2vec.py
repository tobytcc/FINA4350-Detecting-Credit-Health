# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:17:32 2023

@author: Toby Chiu
"""

from gensim.models import word2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex
import pickle

# get the textlist
with open('text-list.pickle', 'rb') as myfile:
    textList = pickle.load(myfile)
myfile.close()

# model for word embeddings
model = Doc2Vec([TaggedDocument(doc, [i]) for i, doc in enumerate(textList)], workers = 2, min_count = 3)
similar_word = model.wv.most_similar('default')
print(similar_word)

# testing data
with open('testing-data.pickle', 'rb') as myfile:
    testData = pickle.load(myfile)
myfile.close()


# create dictinoary
documents = []
for doc in testData:
    if doc in model: 
        documents.append(doc)
dictionary = Dictionary(documents)

documents = [dictionary.doc2bow(doc) for doc in documents]

# create tf-idf model
tfidf = TfidfModel(documents)
documents = [tfidf[doc] for doc in documents]

# SCM
termsim_index = WordEmbeddingSimilarityIndex(model)
termsim_matrix = SparseTermSimilarityMatrix(termsim_index, dictionary, tfidf)

def SCM(docA, docB):
    similarity = termsim_matrix.inner_product(docA, docB, normalized=(True, True))
    
# testing

for ind in range(len(textList)):
    joinedText = ' '.join(textList[ind])
    textList[ind] = joinedText
    
for ind in range(len(testData)):
    joinedText = ' '.join(testData[ind])
    testData[ind] = joinedText

print([SCM(textList[0], test) for test in testData])