#!/usr/bin/env python

from nltk.tokenize.punkt import PunktWordTokenizer
import Keyword

class Parser:
    def __init__(self, text):
        """Initialize parser"""
        self._corpus = text
        pass

    def replace_indices(self, indices, text):
        """Replace the indices of the tokenized text"""
        text_tokens = PunktWordTokenizer().tokenize(text)

        result = [token.replace(filter(str.isalnum, token), )]
        
        for index in indices:
            text_tokens[index] = text_tokens[index].replace(filter(str.isalnum, text_tokens[index]),
                                                            Keyword.Keyword("N", self._corpus, filter(str.isalnum, text_tokens[index])).word_rank(0))

        return result

    
