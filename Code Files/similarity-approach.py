# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:17:32 2023

@author: Toby Chiu
"""

from gensim.models import word2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import SoftCosineSimilarity, SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex
import pickle

# get the textlist
with open('text-list.pickle', 'rb') as myfile:
    textList = pickle.load(myfile)
myfile.close()

with open('existing-dic.pickle', 'rb') as myfile:
    existing_dic = pickle.load(myfile)
myfile.close()

# model for word embeddings
model = Doc2Vec([TaggedDocument(doc, [i]) for i, doc in enumerate(textList)], workers = 2, min_count = 2)
modelvocab = list(model.wv.key_to_index.keys())
similar_word = model.wv.most_similar('default', topn=20) 
print(similar_word)

# testing data
with open('5-2_testingdata_v1.pickle', 'rb') as myfile:
    testData = pickle.load(myfile)
myfile.close()
testData = [test.split() for test in testData]

#remove out-of-vocabulary words
i = 0
for doc in testData:
    tempList = [w for w in doc if w in modelvocab]
    testData[i] = tempList
    i += 1

# create dictinoary
documents = []
for doc in testData:
    documents.append(doc)
dictionary = Dictionary(documents)

documents = [dictionary.doc2bow(doc) for doc in documents]

# create tf-idf model
tfidf = TfidfModel(documents)
words = [word for word, count in dictionary.most_common()]
word_vectors = model.wv.vectors_for_all(words, allow_inference=False)
documents = [tfidf[doc] for doc in documents]

# Soft Cosine Measurement (SCM)
termsim_index = WordEmbeddingSimilarityIndex(word_vectors)
termsim_matrix = SparseTermSimilarityMatrix(termsim_index, dictionary, tfidf)
    
def SCM(docA, docB):
    return termsim_matrix.inner_product(docA, docB, normalized=(True, True))

print(list([SCM(tfidf[dictionary.doc2bow(textList[1])], doc) for doc in documents]))