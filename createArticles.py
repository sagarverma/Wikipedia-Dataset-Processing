import os
import articleSegmenter as aS
import re
from os import path, listdir
import sys

WIKI_FILES_DIR = path.join(path.dirname(__file__), "wikipedia/wikipedia4/")
ARTICLES_OUT_DIR = path.join(path.dirname(__file__), "wikiclean/wikipedia4/")

tmp = listdir(WIKI_FILES_DIR)
wiki_files_list = []
for item in tmp:
	wiki_files_list.append(item)
	name = item[17:-4]
	if not os.path.exists(ARTICLES_OUT_DIR + name):
		os.mkdir(ARTICLES_OUT_DIR + name)
wiki_files_list.sort()

for filename in wiki_files_list:
	CURRENT_DIR = ARTICLES_OUT_DIR + filename[17:-4] + "/"
	fin = open(WIKI_FILES_DIR + filename, 'r')
	filedata = fin.read()
	fin.close()
	articles,titles = aS.articleSegment(filedata)
	for title in titles:
		#outsys =  "Creating article " + title + " inside " + CURRENT_DIR
		#print outsys
		outfilename = re.sub('[/\:;*?"<>|%,#$!+{}&.,]','',title)
		if len(outfilename) > 250:
			outfilename = outfilename[:250]
		fout = open(CURRENT_DIR + outfilename + ".txt", "w")
		fout.write(articles[title])
		fout.close()

