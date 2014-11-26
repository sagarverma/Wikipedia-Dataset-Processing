from pymongo import MongoClient, Connection
import ast
from os import listdir

client = MongoClient()
db = client.wiki
articles = db.articles

fin = open('test/index/index.txt','r')
data = fin.read().split('\n')
index = {}
for d in data:
	t = map(str, d.split(':'))
	index[t[1]] = t[0]


folders = listdir("test/articles/")

for folder in folders:
	files = listdir("test/articles/" + folder)
	for filename in files:
		an = long(index[filename])
		data = open("test/articles/" + folder + "/" + filename, "r").read()
		article_id = articles.insert({'_id':an,'a':data})
		print article_id
