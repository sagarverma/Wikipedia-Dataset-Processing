from os import path, listdir

TAGGED_FILES_DIR = path.join(path.dirname(__file__), "tagged/wikipedia4/")
TAGGED_FILES_OUT = path.join(path.dirname(__file__), "tagged/nwikipedia4/")

tmp = listdir(TAGGED_FILES_DIR)
tagged_files_list = []
for item in tmp:
	tagged_files_list.append(item)
tagged_files_list.sort()

print len(tagged_files_list)
for filename in tagged_files_list:
	fin = open(TAGGED_FILES_DIR + filename, 'r')
	fout = open(TAGGED_FILES_OUT+ "n" + filename[:-3] + "csv", 'w')
	for line in fin:
		temp = line.split()
		if len(temp) >= 2 :
			fout.write(temp[0] + '	' + temp[1] + "\n")
		else:
			fout.write(temp[0] + "\n")
	fin.close()
	fout.close()
	fin = open(TAGGED_FILES_DIR + filename, 'w')
	fin.close()
