from multiprocessing import Process
from nltk import pos_tag
from nltk.corpus import stopwords
from os import path, listdir, mkdir
from re import findall, sub
from math import ceil

stop = stopwords.words('english')
others = ['` `',',','"',':','[',']','.','>','<','/','?','|','\\','{','}','=','+','-','_','~','`','" "','!','@','#','$','%','^','&','*','(',')']

PATTERN = "[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+"

VERBS_NOUNS = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ']
folders = listdir("wikiarticles/wikipedia5")

index = {}
findex = open('index.txt','r')
data  = findex.read()
findex.close()
data = data.split('\n')
for d in data:
	t = map(str, d.split(':'))
	index[t[1]] = t[0]

print len(index)
def process_folders(folders):
	for folder in folders:
		if not path.exists("res/wikipedia5/" + folder):
			mkdir("res/wikipedia5/" + folder)
		files = listdir("wikiarticles/wikipedia5/"+folder)
		for filename in files:
			article_no = index[filename]
			fin = open("wikiarticles/wikipedia5/"+folder+"/"+filename,"r")
			data = fin.read()
			data = data.lower()
			fin.close()
			size = len(data)
			chunks = int(ceil(size/2500.0))
			#print chunks
			out = ""
			for i in range(1,chunks+1):
				temp = ""
				if i == 1:
					temp = data[:2500 + 60]
				else:
					temp = data[((i-1)*2500)-60:(i*2500)+60]
				seen_words = {}
				words = findall(PATTERN, temp)
				tags = pos_tag(words)
				for tag in tags:
					if tag[0] not in stop and tag[0] not in others and tag[1] in VERBS_NOUNS:
						if tag[0] not in seen_words:
							seen_words[tag[0]] = [tag[1]]
						elif tag[1] not in seen_words[tag[0]]:
							seen_words[tag[0]].append(tag[1])
				for k,v in  seen_words.items():
					out += k + " " + article_no + "." + str(1) + " " + str(v) + "\n"
			fout = open("res/wikipedia5/"+folder+"/"+filename,"w")
			fout.write(out)
			fout.close()
			
folderr = []
for folder in folders:
	folderr.append(folder)
folderr.sort()
folders = []
Process(target=process_folders, args=(folderr[18:100],)).start()
Process(target=process_folders, args=(folderr[118:200],)).start()
Process(target=process_folders, args=(folderr[218:300],)).start()
Process(target=process_folders, args=(folderr[318:400],)).start()
Process(target=process_folders, args=(folderr[419:500],)).start()
Process(target=process_folders, args=(folderr[520:600],)).start()
Process(target=process_folders, args=(folderr[617:700],)).start()
#Process(target=process_folders, args=(folderr[728:800],)).start()
#Process(target=process_folders, args=(folderr[800:900],)).start()
#Process(target=process_folders, args=(folderr[900:1000],)).start()