from re import findall
from os import path, listdir, mkdir

PATTERN1 = r'==(.*)\n'
PATTERN2 = r'\[\[(.*)\]\]\n'
PATTERN3 = '==References=='
PATTERN4 = '==Summary=='
PATTERN5 = '==Licensing=='
PATTERN6 = '\n*'

WIKIARTICLES_DIR = path.join(path.dirname(__file__), "wikiclean/")
WIKICLEAN_DIR = path.join(path.dirname(__file__), "wikiarticles/")

parts = listdir(WIKIARTICLES_DIR)
partt = []
for part in parts:
	partt.append(part)
partt.sort()
parts = []

for part in partt:
    print part
    if not path.exists(WIKICLEAN_DIR + part):
        mkdir(WIKICLEAN_DIR + part)
    folders = listdir(WIKIARTICLES_DIR + part + "/")
    folderr = []
    for folder in folders:
        folderr.append(folder)
    folderr.sort()
    fodlers = []

    for folder in folderr:
        print folder
        if not path.exists(WIKICLEAN_DIR + part + "/" + folder):
                mkdir(WIKICLEAN_DIR + part + "/" + folder)
        articles = listdir(WIKIARTICLES_DIR + part + "/" + folder + "/")
        articlee = []
        for article in articles:
            articlee.append(article)
        articlee.sort()
        articles = []

        for article in articlee:
            if not path.exists(WIKICLEAN_DIR + part + "/" + folder + "/" + article):
                #print folder
                fin = open(WIKIARTICLES_DIR + part + "/" + folder + "/" + article, 'r')
                data = fin.read()
                fin.close()
                data = data.replace(PATTERN6, '\n')
                if PATTERN3 in data:
                    pos = data.index(PATTERN3)
                    data = data[:pos]
                if PATTERN4 in data:
                    pos = data.index(PATTERN4)
                    data = data[:pos]
                if PATTERN5 in data:
                    pos = data.index(PATTERN5)
                    data = data[:pos]
                titles = findall(PATTERN2, data)
                for title in titles:
                    data = data.replace("[["+title+"]]\n",'')
                headings = findall(PATTERN1, data)
                for heading in headings:
                    data = data.replace("=="+heading, '')
                data = data.split('\n')
                out = ''
                for item in data:
                    if len(item) > 5:
                        out += item    
                        out += '\n'
                fout = open(WIKICLEAN_DIR + part + "/" + folder + "/" + article, 'w')
                fout.write(out)
                fout.close()
                    
