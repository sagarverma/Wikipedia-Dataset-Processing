import articleSegmenter as aS
import re
from os import path, listdir
from nltk.corpus import treebank_raw
import nltk
import string
from datetime import datetime
from corenlp import *
from simplejson import loads
import unicodedata
import codecs

def convert(line):
	return ''.join([i if ord(i) < 128 else '' for i in line])

nlp = StanfordCoreNLP()

tstart = datetime.now()

TAG_DIR = path.join(path.dirname(__file__), "tagged/")
WIKI_FILES_DIR = path.join(path.dirname(__file__), "wikipedia/")

tmp = listdir(WIKI_FILES_DIR)
wiki_files_list = []
for item in tmp:
	wiki_files_list.append(item)
wiki_files_list.sort()

tagset_map = {'CC':'CC','CD':'CD','DT':'DT','EX':'EX','IN':'IN','JJ':'JJ','JJR':'JJR','JJS':'JJS','LS':'LS','MD':'MD','NN':'NN','NNS':'NNS','NNP':'NNP','NNPS':'NNPS','PDT':'PDT','POS':'POS','PRP':'PRP','PRP$':'PRPd','RB':'RB','RBR':'RBR','RBS':'RBS','RP':'RP','SYM':'SYM','TO':'TO','UH':'UH','VB':'VB','VBD':'VBD','VBG':'VBG','VBN':'VBN','VBP':'VBP','VBZ':'VBZ','WDT':'WDT','WP':'WP','WP$':'WPd','WRB':'WRB'}

tagset_files = {}

fcc = open(TAG_DIR+'CC','a')
fcd = open(TAG_DIR+'CD','a')
fdt = open(TAG_DIR+'DT','a')
fex = open(TAG_DIR+'EX','a')
fin = open(TAG_DIR+'IN','a')
fjj = open(TAG_DIR+'JJ','a')
fjjr = open(TAG_DIR+'JJR','a')
fjjs = open(TAG_DIR+'JJS','a')
fls = open(TAG_DIR+'LS','a')
fmd = open(TAG_DIR+'MD','a')
fnn = open(TAG_DIR+'NN','a')
fnns = open(TAG_DIR+'NNS','a')
fnnp = open(TAG_DIR+'NNP','a')
fnnps = open(TAG_DIR+'NNPS','a')
fpdt = open(TAG_DIR+'PDT','a')
fpos = open(TAG_DIR+'POS','a')
fprp = open(TAG_DIR+'PRP','a')
fprpd = open(TAG_DIR+'PRPd','a')
frb = open(TAG_DIR+'RB','a')
frbr = open(TAG_DIR+'RBR','a')
frbs = open(TAG_DIR+'RBS','a')
frp = open(TAG_DIR+'RP','a')
fsym = open(TAG_DIR+'SYM','a')
fto = open(TAG_DIR+'TO','a')
fuh = open(TAG_DIR+'UH','a')
fvb = open(TAG_DIR+'VB','a')
fvbd = open(TAG_DIR+'VBD','a')
fvbg = open(TAG_DIR+'VBG','a')
fvbn = open(TAG_DIR+'VBN','a')
fvbp = open(TAG_DIR+'VBP','a')
fvbz = open(TAG_DIR+'VBZ','a')
fwdt = open(TAG_DIR+'WDT','a')
fwp = open(TAG_DIR+'WP','a')
fwpd = open(TAG_DIR+'WPd','a')
fwrb = open(TAG_DIR+'WRB','a')		
fstop = open(TAG_DIR+'STOP','a')

tagset_file = {'CC':fcc,'CD':fcd,'DT':fdt,'EX':fex,'IN':fin,'JJ':fjj,'JJR':fjjr,'JJS':fjjs,'LS':fls,'MD':fmd,'NN':fnn,'NNS':fnns,'NNP':fnnp,'NNPS':fnnps,'PDT':fpdt,'POS':fpos,'PRP':fprp,'PRP$':fprpd,'RB':frb,'RBR':frbr,'RBS':frbs,'RP':frp,'SYM':fsym,'TO':fto,'UH':fuh,'VB':fvb,'VBD':fvbd,'VBG':fvbg,'VBN':fvbn,'VBP':fvbp,'VBZ':fvbz,'WDT':fwdt,'WP':fwp,'WP$':fwpd,'WRB':fwrb}

article_no = 0

for file_name in wiki_files_list[:2]:
	if "wiki-en_00" in file_name:
		fstart = datetime.now()
		f = open("wikipedia/"+file_name,'r')
		#f = codecs.open("test", encoding='utf-8')	
		#f = open('wikiclean/20140615-wiki-en_000000.txt','r')	
		data = f.read().decode(encoding="utf-8", errors="ignore").encode(encoding="ascii", errors="ignore")
		f.close()
		#data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
		articles,titles = aS.articleSegment(data)
		for i in range(len(articles)):
			print titles[i] + "		of file		" + file_name
			astart = datetime.now()			
			lines = articles[titles[i]].split("\n")
			for line in lines:
				result = nlp.parse(line)
			article_no += len(articles)
			aend = datetime.now()
			print (aend-astart).seconds
		article_no += len(articles)
		fend = datetime.now()
		print (fend-fstart).seconds

tend = datetime.now()
print (tend-tstart).seconds

