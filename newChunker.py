from os import listdir, mkdir, path
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = stopwords.words('english')
others = ['` `',',','"',':','[',']','.','>','<','/','?','|','\\','{','}','=','+','-','_','~','`','" "','!','@','#','$','%','^','&','*','(',')']

CHUNK_SIZE = 2500
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
		folderr.append(folder)
	folderr.sort()
	folders = []
	
	for folder in folderr:
		if not path.exists("compressed/" + part + "/" + folder):
			mkdir("compressed/" + part + "/" + folder)
		
		files = listdir("wikiarticles/" + part + "/" + folder + "/")
		filee = []
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []
		
		for filename in filee:
			article_no += 1
			fin = open("wikiarticles/" + part + "/" + folder + "/" + filename, "r")
			data = fin.read()
			fin.close()
			out = ""
			size = len(data)
			chunks = size/CHUNK_SIZE
			if len(data) > CHUNK_SIZE:
				temp = data[0:CHUNK_SIZE + 60]
			else:
				temp = data[0:]
			words = word_tokenize(temp)
			curr_chunk = {}
			for word in words:
				word = word.lower()
				if word not in stop and word not in others and word not in curr_chunk:
					curr_chunk[word] = 1
					out += word + "," + str(article_no) + ".1\n"
			for j in range(1,chunks-1):
				curr_chunk = {}
				temp = data[j*CHUNK_SIZE - 60 : ((j+1) * CHUNK_SIZE) + 60]
				words = word_tokenize(temp)
				for word in words:
					word = word.lower()
					if word not in stop and word not in others and word not in curr_chunk:
						curr_chunk[word] = 1
						out += word + "," + str(article_no) + "." + str(j+1) + "\n" 			
			temp = data[(chunks-1)*CHUNK_SIZE:]
			words = word_tokenize(temp)
			curr_chunk = {}
			for word in words:
				word = word.lower()
				if word not in stop and word not in others and word not in curr_chunk:
					curr_chunk[word]= 1
					out += word + "," + str(article_no) + "." + str(chunks) + "\n"
			
			fout = open("compressed/" + part + "/" + folder + "/" + filename, "w")
			fout.write(out)
			fout.close()
