from os import listdir

folders = listdir("compressed/wikipedia1/")
folderr = []
for folder in folders:
	folderr.append(folder)
folderr.sort()
folders = []

for folder in folderr:
	files = listdir("compressed/wikipedia1/" + folder + "/")
	fout = open("joined/wikipedia1/" + folder , "w")
	filee = []
	for filename in files:
		filee.append(filename)
	filee.sort()
	files = []
	
	for filename in filee:
		fin = open("compressed/wikipedia1/" + folder + "/" + filename, "r")
		data = fin.read()
		fin.close()
		fout.write(data)
	
	fout.close()
