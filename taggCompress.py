from os import listdir
from ast import literal_eval

TAG_IN = "TestSet/tagged/"

fout = open("TestSet/taggCompress.txt", "w")
data = {}
folders = listdir(TAG_IN)
for folder in folders:
	files = listdir(TAG_IN + folder + "/")
	for filename in files:
		fin = open(TAG_IN + folder + "/" + filename, "r")
		filedata = literal_eval(fin.read())
		fin.close()
		for k,v in filedata.items():
			if k not in data:
				data[k] = v
fout.write(str(data))
fout.close()
		