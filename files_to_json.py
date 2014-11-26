from os import listdir
from math import ceil

parts = listdir("wikiarticles/")
partt = []
for part in parts:
	partt.append(part)
partt.sort()
parts = []

article_id = 0

for part in partt:
	mkdir("chunks/"+part)
	folders = listdir("wikiarticles/" + part)
	folderr = []
	for folder in folders:
		folderr.append(folder)
	folderr.sort()
	folders = []

	for folder in folderr:
		fout = open("chunks/"+part+"/"+folder+".json")
		files = listdir("wikiarticles/"+part+"/"+folder)
		filee = []
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []

		for filename in filee:
			article_id += 1
			data = open("wikiarticles/"+part+"/"+folder+"/"+filename)
			size = len(data)
			chunks = ceil(len(data)/2500)
			for i in range(chunks):
				chunk['_id'] = float(str(article_id)+'.'+str(i+1))
				chunk['c'] = data[i*2500:(i+1)*2500]
				fout.write(str(chunk) + "\n")

		fout.close()