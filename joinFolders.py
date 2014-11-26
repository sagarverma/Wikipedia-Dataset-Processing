from os import listdir

files = listdir("joined/wikipedia1/")
filee = []
for filename in files:
	filee.append(filename)
filee.sort()
files = []

fout = open("joined/part1.txt", "w")
	
for filename in filee:
	fin = open("joined/wikipedia1/" + filename, 'r')
	fout.write(fin.read())
	fin.close()

fout.close()
