import articleSegmenter as aS
import re
from os import path, listdir
from nltk.corpus import treebank_raw
import nltk
import string
from datetime import datetime


tstart = datetime.now()

sents = treebank_raw.sents()
tokens = []
boundaries = set()
offset = 0
for sent in sents:
	tokens.extend(sent)
	offset += len(sent)
	boundaries.add(offset-1)

def punct_features(tokens, i):
	return {'next-word-capitalized': tokens[i+1][0].isupper(),
			'prev-word': tokens[i-1].lower(),
			'punt': tokens[i],
			'prev-word-is-one-char': len(tokens[i-1]) == 1}

featuresets = [(punct_features(tokens, i), (i in boundaries))
				for i in range(1, len(tokens)-1)
				if tokens[i] in '.?!']

classifier = nltk.NaiveBayesClassifier.train(featuresets)

def segment_sentences(words):
	start = 0
	sents = []
	for i, word in enumerate(words):
		if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
			sents.append(words[start:i+1])
			start = i+1
	if start < len(words):
		sents.append(words[start:])
	return sents


TAG_DIR = path.join(path.dirname(__file__), "tagged/")
WIKI_FILES_DIR = path.join(path.dirname(__file__), "wikipedia")

tmp = listdir(WIKI_FILES_DIR)
wiki_files_list = []
for item in tmp:
	wiki_files_list.append(item)
wiki_files_list.sort()

tagset_map = {'CC':'CC','CD':'CD','DT':'DT','EX':'EX','IN':'IN','JJ':'JJ','JJR':'JJR','JJS':'JJS','LS':'LS','MD':'MD','NN':'NN','NNS':'NNS','NNP':'NNP','NNPS':'NNPS','PDT':'PDT','POS':'POS','PRP':'PRP','PRP$':'PRPd','RB':'RB','RBR':'RBR','RBS':'RBS','RP':'RP','SYM':'SYM','TO':'TO','UH':'UH','VB':'VB','VBD':'VBD','VBG':'VBG','VBN':'VBN','VBP':'VBP','VBZ':'VBZ','WDT':'WDT','WP':'WP','WP$':'WPd','WRB':'WRB'}

tagset_files = {}

fcc = open(TAG_DIR+'CC','w')
fcd = open(TAG_DIR+'CD','w')
fdt = open(TAG_DIR+'DT','w')
fex = open(TAG_DIR+'EX','w')
fin = open(TAG_DIR+'IN','w')
fjj = open(TAG_DIR+'JJ','w')
fjjr = open(TAG_DIR+'JJR','w')
fjjs = open(TAG_DIR+'JJS','w')
fls = open(TAG_DIR+'LS','w')
fmd = open(TAG_DIR+'MD','w')
fnn = open(TAG_DIR+'NN','w')
fnns = open(TAG_DIR+'NNS','w')
fnnp = open(TAG_DIR+'NNP','w')
fnnps = open(TAG_DIR+'NNPS','w')
fpdt = open(TAG_DIR+'PDT','w')
fpos = open(TAG_DIR+'POS','w')
fprp = open(TAG_DIR+'PRP','w')
fprpd = open(TAG_DIR+'PRPd','w')
frb = open(TAG_DIR+'RB','w')
frbr = open(TAG_DIR+'RBR','w')
frbs = open(TAG_DIR+'RBS','w')
frp = open(TAG_DIR+'RP','w')
fsym = open(TAG_DIR+'SYM','w')
fto = open(TAG_DIR+'TO','w')
fuh = open(TAG_DIR+'UH','w')
fvb = open(TAG_DIR+'VB','w')
fvbd = open(TAG_DIR+'VBD','w')
fvbg = open(TAG_DIR+'VBG','w')
fvbn = open(TAG_DIR+'VBN','w')
fvbp = open(TAG_DIR+'VBP','w')
fvbz = open(TAG_DIR+'VBZ','w')
fwdt = open(TAG_DIR+'WDT','w')
fwp = open(TAG_DIR+'WP','w')
fwpd = open(TAG_DIR+'WPd','w')
fwrb = open(TAG_DIR+'WRB','w')		
fstop = open(TAG_DIR+'STOP','w')

tagset_file = {'CC':fcc,'CD':fcd,'DT':fdt,'EX':fex,'IN':fin,'JJ':fjj,'JJR':fjjr,'JJS':fjjs,'LS':fls,'MD':fmd,'NN':fnn,'NNS':fnns,'NNP':fnnp,'NNPS':fnnps,'PDT':fpdt,'POS':fpos,'PRP':fprp,'PRP$':fprpd,'RB':frb,'RBR':frbr,'RBS':frbs,'RP':frp,'SYM':fsym,'TO':fto,'UH':fuh,'VB':fvb,'VBD':fvbd,'VBG':fvbg,'VBN':fvbn,'VBP':fvbp,'VBZ':fvbz,'WDT':fwdt,'WP':fwp,'WP$':fwpd,'WRB':fwrb}

article_no = 0

for file_name in wiki_files_list[:2]:
	if "wiki-en_00" in file_name:
		#print "here"
		fstart = datetime.now()
		f = open("wikipedia/"+file_name, 'r')
		data = f.read()
		f.close()
		data = filter(lambda x:x in string.printable, data)
		articles,titles = aS.articleSegment(data)
		for i in range(len(articles)):
			print titles[i] + "		of file		" + file_name
			sents = segment_sentences(articles[titles[i]])
			for j in range(len(sents)):
				tokens = nltk.word_tokenize(sents[j])
				tags = nltk.pos_tag(tokens)
				#print len(tags)
				#print tags
				for k in range(len(tags)):
					if tags[k][1] in tagset_file:
						ftemp = tagset_file[tags[k][1]]
					else:
						ftemp = fstop
					ftemp.write('"'+ tags[k][0] + '"		:[' + str(article_no + i + 1) + ',' + str(j + 1) + ',' + str(k + 1) + "],\n")
					#print ftemp
		article_no += len(articles)
		fend = datetime.now()
		print (fend-fstart).seconds

tend = datetime.now()
print (tend-tstart).seconds

