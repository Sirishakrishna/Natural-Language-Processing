import nltk
#nltk.download('punkt')
text="CR Rao Advanced Institute of Mathematics Statistics and Computer Science"
#import functions word_tokenize, sent_tokenize from the module nltk.tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
sents=word_tokenize(text)
print(sents)

