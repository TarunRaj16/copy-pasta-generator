#!/usr/bin/env python
import nltk
from nltk.corpus import brown
import random

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
        listOne = [replacee]
        return nltk.pos_tag(listOne)[0][1]
    
    def access(self, distance, fuzziness, new_theme, replacee, replacee_pos):
        """Fuzzily access the word at a certain distance away"""
        if distance == -1:
            return self.access_backup(replacee, replacee_pos)
        
        for similar_word_list in new_theme._similar_word_lists:
            for ii in [int(round(jj * (-0.5 if jj%2 == 0 else 0.5))) for jj in range(0,fuzziness * 2) ]:
                if distance + ii < 0 or distance + ii > len(similar_word_list):
                    continue
                if self.find_pos(similar_word_list[distance + ii]) == replacee_pos:
                    return similar_word_list[distance + ii]

        for similar_word_list in new_theme._similar_word_lists:
            for ii in [int(round(jj * (-0.5 if jj%2 == 0 else 0.5))) for jj in range(0,fuzziness * 2) ]:
                if distance + ii < 0 or distance + ii > len(similar_word_list):
                    continue
                if self.find_pos(similar_word_list[distance + ii])[0:2] == replacee_pos[0:2]:
                    return similar_word_list[distance + ii]

        # return("not found")
        return self.access_backup(replacee, replacee_pos)

    def access_backup(self, to_replace, pos):
        new_list = self._corpus.similar_words(to_replace, 50)
        for wordy in new_list:
            if (self.find_pos(wordy)) == pos:
                return wordy
        for wordy in new_list:
            if (self.find_pos(wordy))[0:2] == pos[0:2]:
                return wordy    
        return new_list[random.randint(0,9)]

    
    def replace(self, new_theme, to_replace, pos):
    	print("Replacing {0} which is a {1}".format(to_replace, pos))
        return new_theme.access(self.distance(to_replace), 25, new_theme, to_replace, pos)
                

##def main():
##    textG = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
##    stuff = ["frozen"]
##    pi = Theme(textG, stuff)
##    
####    print(nltk.pos_tag(stuff)[0][1])
##    for list1 in pi._similar_word_lists:
##        for word in list1:
##            print(word)
##
##if __name__=="__main__":
##    main()
   
