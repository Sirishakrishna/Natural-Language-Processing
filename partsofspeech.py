import nltk
#nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize, sent_tokenize

text="sirisha worked in the areas of graph analytics"

st=nltk.pos_tag(word_tokenize(text))
print(st)