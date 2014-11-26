from os import listdir, mkdir, path
from nltk import word_tokenizer
from nltk.corpus import stopwords

stop = stopwords.wrods('english')
others = ['` `',',','"',':','[',']','.','>','<','/','?','|','\\','{','}','=','+','-','_','~','`','" "','!','@','#','$','%','^','&','*','(',')']

CHUNK_SIZE = 
article_no = 0

parts = listdir("wikiarticles/")
partt = []
for part in parts:
	partt.append(part)
partt.sort()
parts = []

for part in partt:
	if not path.exists("compressed/" + part):
		mkdir("compressed/" + part)
	
	folders = listdir("wikiarticles/" + part + "/")
	folderr = []
	for folder in folders:
		if 
		folderr.append(folder)
	folderr.sort()
	folders = []
	
	for folder in folderr:
		if not path.exists("compressed/" + part + "/" + folder):
			mkdir("compressed/" + part + "/" + folder)
		
		files = listidr("wikiarticles/" + part + "/" + "folder" + "/")
		filee - []
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []
		
		for filename in filee:
			fin = open("wikiarticles/" + part + "/" + "folder" + "/" + filename, "r")
			data = fin.read()
			fin.close()
			size = len(tokens) 
		
	
