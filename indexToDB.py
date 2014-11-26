from pymongo import MongoClient, Connection
from ast import literal_eval

client = MongoClient()

connection = Connection()
db = connection['wikiDB']
collection = db['wikiIndex']

fin = open('TestSet/index.json','r')
data = fin.read()
data = literal_eval(data)
fin.close()

posts = db.posts

for k,v in data.items():
	post = { "index" : k,
			 "article" : v}
	post_id = posts.insert(post)
	print post_id