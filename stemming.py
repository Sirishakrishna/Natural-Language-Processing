import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
text="Sirisha worked in the areas of graph analytics, big data analytics and Currently she is working in the"
"areas of nlp and Artificial Intellegence and her recent works are graph based ciphers, detecting fraudelent"
"patterns in IP network traffic etc"

from nltk.stem.lancaster import LancasterStemmer
st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in word_tokenize(text)]
print(stemmedWords)