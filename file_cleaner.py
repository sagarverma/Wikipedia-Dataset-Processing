from os import path, listdir
import codecs
import unicodedata

def convert(data):
	return ''.join([i if ord(i) < 128 else ' ' for i in data])


TAG_DIR = path.join(path.dirname(__file__), "tagged/")
WIKI_FILES_DIR = path.join(path.dirname(__file__), "wikipedia/")

tmp = listdir(WIKI_FILES_DIR)
wiki_files_list = []
for item in tmp:
	wiki_files_list.append(item)
wiki_files_list.sort()

for file_name in wiki_files_list:
	if "wiki-en_00" in file_name:
		fin = codecs.open("wikipedia/"+file_name, encoding='utf-8')		
		data = fin.read()
		fin.close()
		temp1 = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
		temp2 = convert(temp1)
		fout = open("wikiclean/"+file_name, 'w')
		fout.write(temp2)

