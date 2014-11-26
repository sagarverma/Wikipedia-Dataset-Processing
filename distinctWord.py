from os import listdir, mkdir
from nltk import word_tokenize

WIKI_IN = "wikiarticles/wikipedia5/"
WIKI_OUT = "compressed/wikipedia5/"

folders = listdir(WIKI_IN)
folderr = []
for folder in folders:
	mkdir(WIKI_OUT + folder)
	folderr.append(folder)
folderr.sort()
folders = []

for folder in folderr:
	files = listdir(WIKI_IN + folder)
	filee = []
	for filename in files:
		filee.append(filename)
	filee.sort()
	files = []
	
	for filename in filee:
		fin = open(WIKI_IN + folder + "/" + filename, "r")
		data = {}
		line_no = 0
		for line in fin:
			line_no += 1
			words = word_tokenize(line)
			word_no = 0
			for word in words:
				word = word.lower()
				word_no += 1
				if word not in data:
					data[word] = {line_no:[word_no]}
				else:
					if line_no not in data[word]:
						data[word][line_no] = [word_no]
					else:
						data[word][line_no].append(word_no)
		fin.close()
		fout = open(WIKI_OUT + folder + "/" + filename, "w")
		fout.write(str(data))
		fout.close()
				
