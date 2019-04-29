import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import PorterStemmer
import math
from collections import defaultdict
import pickle 

df = pd.read_csv('combined_crime.csv')

with open ('StopTerms', 'rb') as fp:
    stop_terms = pickle.load(fp)

stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(set(stop_terms))

def clean(df_col):
	df_col = df_col.apply(lambda s:s.lower())
	df_col =  df_col.apply(lambda s:re.sub(r"[_()\\\"#/@;:<>(){}```+=~|.!?,|0-9]", " ", s))   #remove puntuations and symbols
	df_col =  df_col.apply(lambda s:re.sub(r"[_()\\\"#/@;:<>(){}```+=~|.!?,|0-9]", " ", s))   #remove puntuations and symbols
	df_col = df_col.apply(lambda s:word_tokenize(s)) 
	df_col = df_col.apply(lambda s: [w for w in s if w not in stop_words])    #remove stop-words
	ps = PorterStemmer()
	df_col = df_col.apply(lambda s:[ps.stem(w) for w in s])		#stemming
	df_col = df_col.apply(lambda s: [w for w in s if w not in stop_words])    #remove stop-words
	return df_col

df['clean content'] = clean(df['content'])
# print(df.head())

def TermFrequency(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

df['Term Frequency'] = df['clean content'].apply(lambda s:TermFrequency(s))
# print(df['Term Frequency'])
df['Term Frequency'] = df['Term Frequency'].apply(lambda s:{k:v for (k,v) in s.items() if v>=2})  #remove low tf words , threshould=2
# print(df['Term Frequency'])

idf = defaultdict(int)
for doc in df['Term Frequency']:
    for w in doc:
        idf[w] += 1

# print(len(idf))
idf   = {k:k for (k,v) in idf.items() if v>3}  #remove low idf words , threshould>3
idf   = {k:k for (k,v) in idf.items() if k not in stop_terms}
vocab = idf.keys() # the vocabulary (BOW) based on tf and idf score 
# print(len(idf))
# print(vocab)
# exit()

#################dtm1###################
cols = vocab
rows = df['clean content']    
names = df['file']    

columns = [''] + list(vocab)
result1_list = []

for i in range(len(df)):
	# print(names[i])
	wordfreq = [rows[i].count(w) for w in vocab]
	entry = [names[i]]
	entry = entry+ wordfreq
	# print(entry)
	result1_list.append(entry)

result1 = pd.DataFrame(result1_list, columns = columns)
result1.to_csv('dtm1.csv',index=False)

######################dtm2################
cols = list(vocab)
result2_list = []
for i in range(len(vocab)):
	# print(names[i])
	twordfreq = 0
	for j in range(len(rows)):
		twordfreq = twordfreq + rows[j].count(cols[i])
		# print(twordfreq)
	entry = [cols[i]]
	entry = entry + [twordfreq]
	# print(entry)
	result2_list.append(entry)

result2 = pd.DataFrame(result2_list, columns = ['word','count'])
result2.to_csv('dtm2.csv',index=True)

######################pairwise document similarity###########################################

documents = df['content']
documents =  documents.apply(lambda s:re.sub(r"[_()\\\"#/@;:<>(){}```+=~|.!?,|0-9]", " ", s))
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
# print(tfidf_matrix)

from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity(tfidf_matrix, tfidf_matrix))
a = cosine_similarity(tfidf_matrix, tfidf_matrix)
np.savetxt("cosine-document-similarity.csv", a, delimiter=",")

###############################cosine similairty#############################################
documents = df['content']
documents =  documents.apply(lambda s:re.sub(r"[_()\\\"#/@;:<>(){}```+=~|.!?,|0-9]", " ", s))
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

from sklearn.metrics.pairwise import pairwise_distances
print(pairwise_distances(tfidf_matrix, tfidf_matrix, metric='cosine'))
a =pairwise_distances(tfidf_matrix, tfidf_matrix, metric='cosine')
np.savetxt("pairwise-document-similarity.csv", a, delimiter=",")

####################################word cloud#######################
with open("WordCloud.txt", 'w') as f:
    for s in vocab:
        f.write(str(s) + '\n')