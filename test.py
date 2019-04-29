# documents = (
# "The sky is blue",
# "The sun is bright",
# "The sun in the sky is bright",
# "We can see the shining sun, the bright sun"
# )

# from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
# print(tfidf_matrix.shape)


# from sklearn.metrics.pairwise import cosine_similarity
# print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix))

import numpy as np
stop_terms = [ 'his' , 'her', 'women', 'child', 
'children', 'men', 'woman', 'man','him', 'sister', 'brother','daughter','son','mom','mother','parent','dad','grandfather','grandmother','young','old','shri',
'gupta','sharma','[',']','&','r','p','c','r','mt','raj','\'',',','/','shin','allow','fir','ii','cr','submit',
'office','rank','one','two','said','say','fair','act','within','and','or','maintain','reject','open','reason','the'
,'u','e','first','second','third','wife','husband','hand','written','result','home','found','ashok','kumar','chndra','khan','pradesh','haryana','end','start',
'think','husband','wife','pw','address','-b','bihar','saw','build','built','address','http','would','shall','dispose'
,'follow','accordingly','made','new','delhi','mumbai','india','house','home','metropoliton',
'already','concern','course','hearing','lodge','bear','also','ms','learn','genuine','member','heard','pecial',
'mention','infere','conclusion','demand','point','along','accept','response','consider','may','mobile','merit','ground','sought','move','regular','day','process',
'six','search','mumbai','chennai','search','object','given','a-','quash','relat','prepare','us','put','clear','fail','far','item','da','g','w','b','p-','p','b','v',
're','crl','right','aware','known','service','evide','feburary','march','april','three','four','five','seven','eight','nine','union','rather','run','etc','reduce',
'look','able','much','close','ajit','keep','guilt','victim','ali','chand','form','ahmedabad','november','brother','years','independent','narayan','laxman','nic',
'judi','facil','anr','fide','pvt','various','value','furnish','cheif','office','bar','offer','lodg','ï¿½','iii','iv','ms','or','rs','-','th','\'s','a-','g','w','b'
'p-','v','scc','arm','pw-','smt','ri','crl','vs','n','ex','j','kg','thu','go','mr','st','bu','ws','rel','rai','lal','tri','urg','l','k','ad','no','slp','f','ï¿½the'
,'incid','dr','abl','amar','led','%','ajit','pc','alia','ladi','nd','bai','h','ed','ion','ce','cm','x','iron','-a','yearsï¿½','pm','juli','laxmi','marayan','lathi',
'suresh','rd','abras','cpc','honï¿½bl','exh','vi','anr','nic','ï¿½','gave','later','december']

stop_terms = [w.lower() for w in stop_terms]

import pickle

with open('StopTerms', 'wb') as fp:
    pickle.dump(stop_terms, fp)

with open ('StopTerms', 'rb') as fp:
    itemlist = pickle.load(fp)

print(itemlist)
