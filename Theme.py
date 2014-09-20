#!/usr/bin/env python
import nltk
from nltk.corpus import brown

class Theme():
    def __init__(self, descriptors):
        """Initialize theme class"""
        self._similar_word_lists = [ self._corpus.similar_words(themes, -1) for descriptor in descriptors ]

    def word_rank(self, num):
        return self._sim_words[num]
    def distance(self, replacee):
        """Calculate the distance between a word and the theme"""
        for similar_word_list in self.similar_word_lists:
            try:
                return similar_word_list.index(replacee)
            except:
                continue
            
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
