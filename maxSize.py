from os import listdir, mkdir, path
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = stopwords.words('english')
others = ['` `',',','"',':','[',']','.','>','<','/','?','|','\\','{','}','=','+','-','_','~','`','" "','!','@','#','$','%','^','&','*','(',')']

MAXX = 0

CHUNK_SIZE = 0
article_no = 0

parts = listdir("wikiarticles/")
partt = []
for part in parts:
	partt.append(part)
partt.sort()
parts = []

for part in partt:
	#if not path.exists("compressed/" + part):
	#	mkdir("compressed/" + part)
	
	folders = listdir("wikiarticles/" + part + "/")
	folderr = []
	for folder in folders:
		folderr.append(folder)
	folderr.sort()
	folders = []
	
	for folder in folderr:
		#if not path.exists("compressed/" + part + "/" + folder):
		#	mkdir("compressed/" + part + "/" + folder)
		
		files = listdir("wikiarticles/" + part + "/" + folder + "/")
		filee = []
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []
		
		for filename in filee:
			fin = open("wikiarticles/" + part + "/" + folder + "/" + filename, "r")
			for line in fin:
				MAXX = max(MAXX,len(line))
		
print MAXX
