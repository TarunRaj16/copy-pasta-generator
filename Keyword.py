#!/usr/bin/env python
import nltk
from nltk.corpus import brown

class keyword():
    def __init__(self, themes):
        """Initialize theme class"""
        self._sim_words1 = self._corpus.similar_words(themes[0], 100)
        self._sim_words2 = self._corpus.similar_words(themes[1], 100)
        self._sim_words3 = self._corpus.similar_words(themes[2], 100)
    def word_rank(self, num):
        return self._sim_words[num]
    def distance(self, replacee):
        if replacee in self._sim_words1:
            return self._sim_words1.index(replacee)
        elif replacee in self._sim_words2:
            return self._sim_words2.index(replacee)
        elif replacee in self._sim_words3:
            return self._sim_words3.index(replacee)
        else:
            return -1
    def access(self, num, replacee)
        pos_type = replacee.get_pos                 """will look into later"""
        if self._sim_words1[num].is_correct_pos:     """will look into later"""
            return self._sim_words1[num]
        for i in range(num, num+20):
            if self._sim_words1[i].is_correct_pos:
                return self._sim_words1[i]
        for i in range(num-20, num-1):
            if self._sim_words1[i].is_correct_pos:
                return self._sim_words1[i]
            
"""
def main():
    textG = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    pi = keyword(None, textG, "kill")
    pi.word_rank(5)

if __name__=="__main__":
    main()
"""   
