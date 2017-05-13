import re
import string
import nltk
import numpy as np

def f1(s, n=3):
    """ Punctuation n-grams """
    regex = re.compile('[^%s]' % re.escape(string.punctuation))
    all_puncs = regex.sub('', s)
    return [all_puncs[i:i+n] for i in range(len(all_puncs)-n+1)]

def f2(s, n=3):
    """ Character n-grams"""
    return [s[i:i+n] for i in range(len(s)-n+1)]

def f3(s, n=50):
    """ n% frequent tokens """
    tokens = nltk.tokenize.word_tokenize(s)
    fdist = nltk.FreqDist(tokens)
    relative_freq = [ key for (key, value) in
            fdist.iteritems() if float(value)/len(tokens) >= float(n)/100]
    return relative_freq

def f4(s, k=2):
    """ Token k-prefixes """
    tokens = nltk.tokenize.word_tokenize(s)
    return [ w[0:k] for w in tokens if len(w) >= k]

def f5(s, k=2):
    """ Token k-suffixes """
    tokens = nltk.tokenize.word_tokenize(s)
    return [ w[-k:] for w in tokens if len(w) >= k]

def f6(s, n=2, k=2):
    """ Token k-prefix n-grams"""
    tokens = nltk.tokenize.word_tokenize(s)
    ngrams = nltk.ngrams(tokens, n)
    return [" ".join(map(lambda x: x[0:k], w)) for w in ngrams if all(np.array(map(len,
        w)) >= k)]


def f7(s, n=2, k=2):
    """ Token k-suffix n-grams"""
    tokens = nltk.tokenize.word_tokenize(s)
    ngrams = nltk.ngrams(tokens, n)
    return [" ".join(map(lambda x: x[-k:], w)) for w in ngrams if all(np.array(map(len,
        w)) >= k)]

def f8_predicate(s, n, k):
    if len(s) == n and len(s) >= k:
        return s[0:n]
    elif len(s) >= n and len(s) >= k:
        return " ".join([s[0:n], s[-k:]])
    return ""

def f8(s, n=2, k=2):
    """ n-prefixes k-suffixes """
    tokens = nltk.tokenize.word_tokenize(s)
    return filter(lambda x: len(x) > 0, map(lambda x: f8_predicate(x, n, k), tokens))


def f9(s, n=3, k=2):
    """ n-suffixes k-prefixes """
    tokens = nltk.tokenize.word_tokenize(s)
    return [" ".join([a[-n:], b[:k]]) for (a, b) in nltk.bigrams(tokens) if len(a) >= n and len(b) >= k]


s = "This.is/a:sample-text"
s1 = "This is a sample text"
s2 = "repeat repeat haha ha bla repeat"

print(f1(s))
print(f2(s1))
print(f3(s2))
print(f4(s1))
print(f5(s1))
print(f6(s1, 2))
print(f7(s1, 2))
print(f8(s1, 2))
print(f9(s1))
