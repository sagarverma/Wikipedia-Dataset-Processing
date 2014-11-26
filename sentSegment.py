from nltk.corpus import treebank_raw
import nltk

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

