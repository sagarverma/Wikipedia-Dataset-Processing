from pymongo import MongoClient, Connection
from ast import literal_eval

client = MongoClient()

connection = Connection()
db = connection['wikiDB']
collection = db['wikiTags']

fin = open('TestSet/taggCompress.json','r')
data = fin.read()
data = literal_eval(data)
fin.close()

tags = data.values()
tags = set(tags)

posts = db.posts

for tag in tags:
	post = { 'tag' : tag }
	post_id = posts.insert(post)
	print post_id