import re
from os import path, listdir
import nltk
import string
from datetime import datetime
import os
from multiprocessing import Process


tstart = datetime.now()

WIKI_FOLDERS_DIR = path.join(path.dirname(__file__), "wikiclean/wikipedia2/")
TAGGED_OUT_DIR = path.join(path.dirname(__file__), "tagged/wikipedia2/")


tmp1 = listdir(WIKI_FOLDERS_DIR)
wiki_folders_list = []
for item in tmp1:
	wiki_folders_list.append(item)
	if not os.path.exists(TAGGED_OUT_DIR + item):
		os.mkdir(TAGGED_OUT_DIR + item)
wiki_folders_list.sort()

def pos_tag_folder(folder):
	tmp2 = listdir(WIKI_FOLDERS_DIR + folder + "/")
	for filename in tmp2:
		if not os.path.isfile(TAGGED_OUT_DIR + folder + "/" + filename):
			#print filename
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
		else:
			pass

for folder in wiki_folders_list[150:250]:
	#print folder
	Process(target=pos_tag_folder, args=(folder,)).start()


tend = datetime.now()
print (tend-tstart).seconds

