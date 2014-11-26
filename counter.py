from os import listdir

WIKI = "compressed/"

parts = listdir(WIKI)
partt = []
for part in parts:
	partt.append(part)
partt.sort()
parts = []
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
			print i
