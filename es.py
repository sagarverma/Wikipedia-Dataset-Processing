import urllib
import urllib2
from os import listdir


files = listdir("wikiarticles")
id = 0
for filename in files:
	id += 1
	values['title'] = filename[:-4]
	values['abstract'] = open("wikiarticles/"+filename,'r').read()[:500]
	values['fileurl'] = "file:///C:/Users/sagar/WikiDataPlay/wikiarticles/" + filename
	#print data
	data = urllib.urlencode(values)
	url = 'http://localhost:9200/wiki/article/' + str(id)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	print response.read()
	values = None
	