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
'suresh','rd','abras','cpc','honï¿½bl','exh','vi','anr','nic','ï¿½','gave','later','december','deepak','al','light','assess','assesse','jain','afresh','especi'
,'gopal','sushil','scrutini','chaudhari','rupe','prejudic','yadav','damag','defin','adjud','notwithstand','ahm','rope','litig','ix','cc','duli','hon∩┐╜bl',
'court∩┐╜','ac','mill','armi','non-compli','manohar','culpabl','pandey','verma','prakash','brother-in-law','uttar','autopsi','ear','contus','pal','chandigarh',
'jaipur','citi','--','inde','gujarat','shed','mandamu'
,'$','patna','student','father-in-law','xxx','reiter','whose','whatev','dr','deliber','da','naduad','co-op','so-cal','son-in-law','lr','mala','nct','vi',
'vii','viii','verma','shashi','ganguli','hr','lr','sr','sri','sl','slp','sd','pawan','mukundakam','leas','sp-cal','lalit','nct','nd',''
'arijit','sirpurkar','raveendran','dey','anand','sri','homicid','alam','bhushan','asok','pasayat','versu','kishor','raw','sd','sr']



stop_terms = [w.lower() for w in stop_terms]

import pickle

with open('StopTerms', 'wb') as fp:
    pickle.dump(stop_terms, fp)

with open ('StopTerms', 'rb') as fp:
    itemlist = pickle.load(fp)

print(itemlist)
