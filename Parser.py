#!/usr/bin/env python

from nltk.tokenize.punkt import PunktWordTokenizer
import Theme

class Parser:
    def __init__(self, text, old_theme_words, new_theme_words):
        """Initialize parser"""
        self._old_theme = Theme.Theme(text, old_theme_words)
        self._new_theme = Theme.Theme(text, new_theme_words)

    def replace_indices(self, indices, text):
        """Replace the indices of the tokenized text"""
        text_tokens = PunktWordTokenizer().tokenize(text)
        pos_tags = nltk.pos_tag(text_tokens)

        # result = [token.replace(filter(str.isalnum, token), )]
        
        for index in indices:
            text_tokens[index] = text_tokens[index].replace(filter(str.isalnum, text_tokens[index]),
                                                            self._old_theme.replace(self._new_theme,
                                                                                    filter(str.isalnum,
                                                                                           text_tokens[index]),
                                                                                    pos_tags[ii][1]),
                                                            )

        return result

    
