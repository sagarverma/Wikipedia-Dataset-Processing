import re



while True:
	inp = str(raw_input())
	out = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", inp)
	print out