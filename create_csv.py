import glob
import pandas as pd

files = []
content = []
file_names = list(glob.glob("HEAD NOTES/*.txt"))
for i in range(1,len(file_names)+1):
	try:
		f = open("HEAD NOTES/"+str(i)+".txt",'rb')
		content.append(f.read().decode(errors='replace'))
		files.append(str(i)+'.txt')
	except:
	 	print(str(i)+'.txt')
print(len(files))
print(len(content))

df = pd.DataFrame({'file':files,'content':content})
df.to_csv('combined_crime.csv',index=False)
