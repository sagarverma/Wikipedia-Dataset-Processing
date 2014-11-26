from os import listdir, mkdir
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = stopwords.words('english')
others = ['/','\\',"'",'"',',','.',';',':','[',']','{','}','|','`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"``","''"]

WIKI_IN = "wikiarticles/"
WIKI_OUT = "newCompressed/"

article_no = 0

def do_it(part):	
	global article_no
	folders = listdir(WIKI_IN + part)
	folderr = []
	for folder in folders:
		mkdir(WIKI_OUT + part + folder)
		folderr.append(folder)
	folderr.sort()
	folders = []
	
	for folder in folderr:
		files = listdir(WIKI_IN + part + folder)
		filee = []
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []
		
		for filename in filee:
			article_no += 1
			fin = open(WIKI_IN + part + folder + "/" + filename, "r")
			data = ""
			line_no = 0
			for line in fin:
				line_no += 1
				words = word_tokenize(line)
				word_no = 0
				for word in words:
					word = word.lower()
					word_no += 1
					if '"' not in word and word not in stop and word not in others:
						data += '"' + word + '",' + str(article_no) + ',' + str(line_no) + ',' + str(word_no) + '\n'
			fin.close()
			fout = open(WIKI_OUT + part + folder + "/" + filename, "w")
			fout.write(data)
			fout.close()

do_it("wikipedia1/")
#do_it("wikipedia2/")
#do_it("wikipedia3/")
#do_it("wikipedia4/")
#do_it("wikipedia5/")
