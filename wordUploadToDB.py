from pymongo import MongoClient, Connection
from ast import literal_eval
from os import listdir

client = MongoClient()
db = client.wiki
words = db.words

data = open("test/words.csv", "r").read().split('\n')
i = 0
for d in data:
	i += 1
	t = map(str, d.split())
	word_id = words.insert({'_id':i,'w':t[0],'ac':float(t[1]),'pt':literal_eval(t[2])})
	print word_id	