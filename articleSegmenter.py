import re

pattern = r'\n\[\[(.*?)\]\]\n\n'
articles = {}
def articleSegment(filedata):
	titles = re.findall(pattern, filedata)
	for i in range(len(titles)):
		if titles.index(titles[i]) == len(titles) - 1:
			articles[titles[i]] = filedata[filedata.index("[["+titles[i]+"]]"):]
		else:
			pos = filedata.index("[["+titles[i]+"]]")
			posnext = filedata.index("[["+titles[i+1]+"]]")
			articles[titles[i]] = filedata[pos:posnext]
	return articles,titles
