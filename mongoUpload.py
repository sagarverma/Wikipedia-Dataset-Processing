from pymongo import MongoClient, Connection

client = MongoClient()
db = client.wiki
collection = db.words
words = db.words

fin = open('000000','r')
i = 0
faults = 0
uni = 0
for line in fin:
	i += 1
	temp = map(str,line.split())
	"""
	if len(temp) > 2:
		faults += 1
	else:
		try:
			post_id = posts.insert({"_id":i, "w":unicode(temp[0],"utf-8"), "ac":float(temp[1])})
		except UnicodeDecodeError:
			uni += 1
	print post_id
	"""
	try:
		post_id = words.insert({"_id":i, "w":unicode(' '.join(temp[0:-1]),"utf-8"), "ac":float(temp[-1])})
	except UnicodeDecodeError:
		uni += 1
	print post_id
print "faults",faults
print "uni",uni