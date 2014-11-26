from os import listdir

WIKI = "wikiarticles/"

parts = listdir(WIKI)
partt = []
for part in parts:
	partt.append(part)
partt.sort()
parts = []
out = ""
i = 0
for part in partt:
	folders = listdir(WIKI + part + "/")
	folderr = []
	for folder in folders:
		folderr.append(folder)
	folderr.sort()
	folders = []
	for folder in folderr:
		files = listdir(WIKI + part + "/" + folder + "/")
		filee = []
		for filename in files:
			filee.append(filename)
		filee.sort()
		files = []
		for filename in filee:
			i += 1
			print str(i) + "	" + filename
			out += str(i) + ":" + filename + "\n"
fout = open("index.txt","w")
fout.write(out)
fout.close()
