import re
from os import path, listdir
import nltk
import string
from datetime import datetime
import os


tstart = datetime.now()

WIKI_FOLDERS_DIR = path.join(path.dirname(__file__), "wikiclean/wikipedia1/")
TAGGED_OUT_DIR = path.join(path.dirname(__file__), "tagged/wikipedia1/")


tmp1 = listdir(WIKI_FOLDERS_DIR)
wiki_folders_list = []
for item in tmp1:
	wiki_folders_list.append(item)
	if not os.path.exists(TAGGED_OUT_DIR + item):
		os.mkdir(TAGGED_OUT_DIR + item)
wiki_folders_list.sort()

for folder in wiki_folders_list:
	#os.mkdir(TAGGED_OUT_DIR + folder)
	tmp2 = listdir(WIKI_FOLDERS_DIR + folder + "/")
	for filename in tmp2:
		fin = open(WIKI_FOLDERS_DIR + folder + "/" + filename, 'r')
		fout = open(TAGGED_OUT_DIR + folder + "/" + filename, 'w')
		out = ""
		i = 0
		for line in fin:
			i += 1
			tokens = nltk.word_tokenize(line)
			tags = nltk.pos_tag(tokens)
			for j in range(len(tags)):
				out += tags[j][1] + " " + tags[j][0] + " " + str(i) + " " + str(j+1) + "\n"
		fout.write(out)
		fout.close()
		fin.close()


tend = datetime.now()
print (tend-tstart).seconds

