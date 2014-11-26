from os import listdir
from ast import literal_eval
import ast
from datetime import datetime

tstart = datetime.now()

COMPRESS_IN = "compressed/wikipedia1/"

findex = open("newIndex.txt", "r")
index = {}
for line in findex:
	temp = map(str, line.split(':'))
	index[temp[1]] = int(temp[0])
findex.close()

tend = datetime.now()

print (tstart-tend).seconds

fout = open("compressed/1compress.txt", "w")

data = {}
folders = listdir(COMPRESS_IN)
folderr = []
for folder in folders:
	folderr.append(folder)
folderr.sort()
folders = []

article_no = 0

for folder in folderr:
	files = listdir(COMPRESS_IN + folder + "/")
	filee = []
	for filename in files:
		filee.append(filename)
	filee.sort()
	files = []
	
	for filename in filee:
		article_no += 1
		fin = open(COMPRESS_IN + folder + "/" + filename, "r")
		filedata = literal_eval(fin.read())
		fin.close()
		for k,v in filedata.items():
			temp = {}
			if k not in data:
				temp[article_no] = v
				data[k] = temp
			else:
				data[k][article_no] = v
				
fout.write(str(data))
fout.close()
		
