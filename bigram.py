import nltk
from nltk.collocations import *
from nltk.tokenize import word_tokenize, sent_tokenize
#Punctuation symbols from the Python string module
from nltk.corpus import stopwords
from string import punctuation
text="be the change you want to see in the world"
customStopWords=set(stopwords.words('english')+list(punctuation))
wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
bigram_measures=nltk.collocations.BigramAssocMeasures()
finder=BigramCollocationFinder.from_words(wordsWOStopwords)
#finder=TrigramCollocationFinder.from_words(wordsWOStopwords)
text1=sorted(finder.ngram_fd.items())
print(text1)


