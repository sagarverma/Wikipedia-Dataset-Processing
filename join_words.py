from os import path, listdir

TAGGED_FILES_DIR = path.join(path.dirname(__file__), "tagged/nwikipedia/")
CLEANED_FILES_OUT = path.join(path.dirname(__file__), "wikiclean/nwikipedia/")

tmp = listdir(TAGGED_FILES_DIR)
tagged_files_list = []
for item in tmp:
	tagged_files_list.append(item)
tagged_files_list.sort()



heads = ['=','==','===','====','=====','======','=======','========']

print len(tagged_files_list)
for filename in tagged_files_list:
	fin = open(TAGGED_FILES_DIR + filename, 'r')
	fout = open(CLEANED_FILES_OUT+ filename[1:-3] + "txt", 'w')
	out = ""
	title_in = 0
	heading_in = 0
	word_count = 0
	count = 0	
	for line in fin:
		temp = line.split()
		if (temp[0] != '[' and temp[0] != ']' and temp[0] != '=' and temp[0] != '*' or temp[0] != ':') and (count <= 70 ):
			out += temp[0]
			out += " "
			count += 1
		elif count <= 70:
			print "here"
			if temp[0] == ']' and title_in == 0:
				title_in = 1
				out += temp[0]
			elif temp[0] == ']' and title_in == 1:
				title_in = 0
				out += temp[0]
				out += "\n"
			elif temp[0] in heads and heading_in == 0:
				heading_in = 1
				out += temp[0]
			elif temp[0] in heads and heading_in == 1:
				heading_in = 0
				out += temp[0]
				out += "\n"
			elif temp[0] == ':':
				out += temp[0]
				out += "\n"
			count += 1
		elif count > 70 and temp[0] == '.':
			out += temp[0]
			out += '\n'
			count = 0
		else:
			out += temp[0]
			out += ' '
			count += 1
	fout.write(out)
	fin.close()
	fout.close()
	
