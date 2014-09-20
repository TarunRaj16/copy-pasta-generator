#!/usr/bin/env python
import nltk
from nltk.corpus import brown

class Theme():
    def __init__(self, text, descriptors):
        """Initialize theme class"""
        self._corpus = nltk.text.ContextIndex(text.tokens)
        self._similar_word_lists = [ self._corpus.similar_words(descriptor, -1) for descriptor in descriptors ]
        
    def word_rank(self, num):
        return self._sim_words[num]
    
    def distance(self, replacee):
        """Calculate the distance between a word and the theme"""
        for similar_word_list in self._similar_word_lists:
            try:
                return similar_word_list.index(replacee)
            except:
                continue
            
        return -1

    def find_pos(self, replacee):
        return "NN"
    
    def access(self, distance, fuzziness, new_theme, replacee, replacee_pos):
        """Fuzzily access the word at a certain distance away"""
        
        for similar_word_list in new_theme.similar_word_lists:
            for ii in [round(jj * (-0.5 if jj%2 == 0 else 0.5)) for jj in range(0,fuzziness * 2) ]:
                if find_pos(similar_word_list[distance + ii]) == replacee_pos:
                    return similar_word_list[distance + ii]
                

def main():
    textG = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    stuff = ["door"]
    pi = Theme(textG, stuff)
    for list1 in pi._similar_word_lists:
        for word in list1:
            print(word)

if __name__=="__main__":
    main()
   

