from pymongo import MongoClient
from nltk import word_tokenize, pos_tag

client = MongoClient()
db = client.wiki
words = db.words
articles = db.articles

while True:
	question = raw_input('Enter Question:')
	tokens = word_tokenize(question)
	for 