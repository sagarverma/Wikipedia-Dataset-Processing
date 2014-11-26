import re
from os import path, listdir, remove

ARTICLES_FOLDERS_DIR = path.join(path.dirname(__file__), "wikiarticles/wikipedia5/")
fout = open('wikipart5_removed_less_than_100_bytes.log','a')
out = ''
wiki_folders = listdir(ARTICLES_FOLDERS_DIR)
for folder in wiki_folders:
	wiki_files = listdir(ARTICLES_FOLDERS_DIR + folder + "/")
	for filename in wiki_files:
		if path.getsize(ARTICLES_FOLDERS_DIR + folder + "/" + filename) < 100L:
			remove(ARTICLES_FOLDERS_DIR + folder + "/" + filename)
			out += (ARTICLES_FOLDERS_DIR + folder + "/" + filename + "\n") 
fout.write(out)
fout.close()