#!/usr/bin/env python
import nltk
from nltk.corpus import brown

class keyword():
    def __init__(self, properties, text, target):
        """Initialize keyword class"""
        self._corpus = nltk.text.ContextIndex(text.tokens)
        self._properties = properties
        self._target = target
    def replace(self):
        simWords = self._corpus.similar_words(self._target, 100)
        print (simWords)

def main():
    textG = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    pi = keyword(None, textG, "cat")
    pi.replace()

if __name__=="__main__":
    main()
    
