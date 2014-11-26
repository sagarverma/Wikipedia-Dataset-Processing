import re
from os import path, listdir
import json

pattern = '\[\[(.*?)\]\]'
def get_titles(data):
	return re.findall(pattern,data)

title_dict = {}
index = 0

WIKI_FILES_DIR = path.join(path.dirname(__file__), "wikipedia")
tmp = listdir(WIKI_FILES_DIR)
wiki_files_list = []
for item in tmp:
	wiki_files_list.append(item)
wiki_files_list.sort()

fout = open('index.json', 'w')
fout.write("{\n")
for file_name in wiki_files_list:
	if "wiki-en_00" in file_name:
		print file_name
		f = open("wikipedia/" + file_name,'r')
		data = f.read()
		f.close()
		temp = get_titles(data)
		for item in temp:
			index += 1
			title_dict[index] = item
			fout.write(' ' + str(index) + ':"' + item + '",\n')

fout.write("}")
fout.close()
print len(title_dict)
