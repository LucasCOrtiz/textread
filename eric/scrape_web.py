#!/home/lucas/anaconda3/envs/py3e/bin/python

#import pandas as pd
#import html5lib
#f_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(f_states[0])
#print(f_states[2])

from newspaper import Article
import newspaper

cnn_paper = newspaper.build('http://cnn.com')
for article in cnn_paper.articles:
   a = Article(article.url, language='en')
   a.download()
   a.parse()
   print(a.text[:200])
