from os import listdir
from re import sub
from ast import literal_eval

NOUNS = ['NN','NNS','NNP','NNPS']
VERBS = ['VB','VBD','VBG','VBN','VBP','VBZ']

fin = open("test/words.txt","r")
fnout = open("test/nouns.csv","w")
fvout = open("test/verbs.csv","w")

data = fin.read()

data = sub(', ',',',data)

for d in data.split('\n'):
	t = map(str, d.split())
	if set(literal_eval(t[2])).intersection(set(NOUNS)):
		fnout.write(t[0]+","+t[1]+'\n')
	if set(literal_eval(t[2])).intersection(set(VERBS)):
		fvout.write(t[0]+","+t[1]+'\n')

fnout.close()
fvout.close()
