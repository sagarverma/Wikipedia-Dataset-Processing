from nltk import word_tokenize
fin = open("A.txt", "r")
data = {}
line_no = 0
for line in fin:
	line_no += 1
	words = word_tokenize(line)
	word_no = 0
	for word in words:
		word = word.lower()
		word_no += 1
		if word not in data:
			data[word] = {line_no:[word_no]}
		else:
			if line_no not in data[word]:
				data[word][line_no] = [word_no]
			else:
				data[word][line_no].append(word_no)
print len(data)
fin.close()
fout = open("A.dat", "w")
fout.write(str(data))
fout.close()