from os import listdir, system, mkdir
from multiprocessing import Process
from nltk import pos_tag, word_tokenize

WIKI_IN = "wikiarticles/"
TAG_OUT = "tagged/"

def postag_part(part):
	folders = listdir(WIKI_IN + part)
	folderr = []
	for folder in folders:
		folderr.append(folder)
	folderr.sort()
	folders = []
	
	for folder in folderr:
		#print folder
		mkdir(TAG_OUT + part + "/" + folder)
		files = listdir(WIKI_IN + part + "/" + folder)
		filee = []		
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []
		for filename in filee:
			data= {}
			fin = open(WIKI_IN + part + "/" + folder + "/" + filename, "r")
			tags = pos_tag(word_tokenize(fin.read()))
			for tag in tags:
				if tag[0].lower() not in data:
					data[tag[0].lower()] = tag[1]
			fin.close()
			fout = open(TAG_OUT + part + "/" + folder + "/" + filename, "w")
			fout.write(str(data))
			fout.close()			

postag_part("wikipedia5") 
