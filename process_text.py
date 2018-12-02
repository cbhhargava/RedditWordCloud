import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def get_tokens(str):
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(str)
    clean_tokens = []
    for w in tokens:
        if w not in stop_words:
            clean_tokens.append(w)
    return clean_tokens