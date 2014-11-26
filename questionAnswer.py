from nltk import pos_tag, NaiveBayesClassifier, FreqDist
from nltk.corpus import stopwords, treebank_raw
from pymongo import MongoClient
from re import findall, sub
import time
from math import log, sqrt

PATTERN = "[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+"

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

classifier = NaiveBayesClassifier.train(featuresets)

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
	
def rank_answers(sentences, question):
	answer_weight_terms = []
	answer_terms_freq = []
	for sentence in sentences:
		sentence = sentence.lower()
		words = findall(PATTERN, sentence)
		word_freq = {}
		for word in words:
			if word not in word_freq:
				word_freq[word] = 1
			else:
				word_freq[word] += 1
		max_freq = max(word_freq.values())
		#print word_freq
		for k,v in word_freq.items():
			word_freq[k] = word_freq[k]/(max_freq * 1.0)
		answer_terms_freq.append(word_freq)
	
	answer_inv_term_freq = {}
	all_terms = {}
	for sentence in sentences:
		sentence = sentence.lower()
		words = set(findall(PATTERN, sentence))
		for word in words:
			if word not in all_terms:
				all_terms[word] = 1
			else:
				all_terms[word] += 1
	for k,v in all_terms.items():
		answer_inv_term_freq[k] = 1 + log((len(sentences)/(v * 1.0)), 2)

	for sentence in answer_terms_freq:
		temp = {}
		for k,v in sentence.items():
			temp[k] = v * answer_inv_term_freq[k]
		answer_weight_terms.append(temp)

	quest_weight_terms = {}
	question = question.lower()
	words = findall(PATTERN, question)
	#print words
	term_freq = {}
	inv_term_freq = {}
	for word in words:
		if word not in term_freq:
			term_freq[word] = 1
		else:
			term_freq[word] += 1
		if word not in inv_term_freq:
			if word in all_terms:
				inv_term_freq[word] = 1 + log((len(sentences) + 1)/((all_terms[word] + 1)*1.0) , 2)
			else:
				inv_term_freq[word] = 1 + log((len(sentences) + 1)/((0 + 1)*1.0) , 2)
	for k,v in term_freq.items():
		quest_weight_terms[k] = v * inv_term_freq[k]

	#print quest_weight_terms
	scores = []
	for sentence in answer_weight_terms:
		#print sentence
		numerator = 0
		t1 = 0
		t2 = 0
		for k,v in quest_weight_terms.items():
			if k in sentence:
				#print k,v
				numerator += v * sentence[k]
				t1 += v**2
				t2 += sentence[k] ** 2
			else:
				#print k,v
				numerator += v * 0
				t1 += v**2
				t2 += 0
		denominator = sqrt(t1) * sqrt(t2)
		#print numerator,denominator
		if numerator == 0 or denominator == 0:
			scores.append(0.0)
		else:
			scores.append(numerator/denominator)

	return scores

client = MongoClient()
db = client.wiki
words = db.words
articles = db.articles

stop = stopwords.words('english')
others = ['` `',',','"',':','[',']','.','>','<','/','?','|','\\','{','}','=','+','-','_','~','`','" "','!','@','#','$','%','^','&','*','(',')']

NOUNS = ['NN','NNS','NNP','NNPS']
VERBS = ['RB','RBR','RBS','RP','VB','VBD','VBG','VBN','VBP','VBZ']
while True:
	question = raw_input('question 	: ')
	question_org = question
	question = question.lower()
	tokens = findall(PATTERN, question)
	#print tokens
	tags = pos_tag(tokens)
	#print tags
	art_chunk = []
	for tag in tags:
		all_words = words.find({'w':tag[0],'pt':tag[1]})
		for word in all_words:
			art_chunk.append(str(word['ac']))
	#print len(art_chunk)

	contents = []
	for ac in art_chunk:
		article_no, chunk_no = map(long, ac.split('.'))
		article = articles.find_one({'_id':article_no})['a']
		chunk = article[(chunk_no-1)*2500:chunk_no*2500]
		contents.append(chunk)

	sentences = contents
	"""
	for content in contents:
		sentences += segment_sentences(content)
	"""
	#print len(sentences)
	answers = []
	scores = rank_answers(sentences,question_org)
	while scores != []:
		curr_score = max(scores)
		#print curr_score
		pos = scores.index(curr_score)
		scores.remove(curr_score)
		answers.append(sentences[pos])

	#print len(answers)
	print len(answers)