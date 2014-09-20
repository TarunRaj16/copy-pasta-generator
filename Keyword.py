#!/usr/bin/env python
import nltk
from nltk.corpus import brown

class keyword():
    def __init__(self, pos, text, target):
        """Initialize keyword class"""
        self._corpus = nltk.text.ContextIndex(text.tokens)
        self._pos = pos
        self._target = target
        self._sim_words = self._corpus.similar_words(self._target, 100)
        self._sim_dict = self._corpus.word_similarity_dict(self._target)
    def word_rank(self, num):
        print(self._sim_words[num])
    def get_pos():
        return self._pos
        

def main():
    textG = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    pi = keyword(None, textG, "kill")
    pi.word_rank(5)

if __name__=="__main__":
    main()
    
