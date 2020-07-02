#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function, find_anagrams(), which can be used to do the same
for an arbitrary list of strings.
"""

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "???"

import sys
import cProfile
import io
import pstats
# from collections import defaultdict

def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # This profiling decorator was adapted from the Python 3.6 Docs
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        string = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=string).sort_stats(sortby)
        ps.print_stats()
        print(string.getvalue())
        return retval

    return inner

def alphabetize(string):
    """Returns alphabetized version of the string."""
    return "".join(sorted(string))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
 #   anagrams = {
 #       alphabetize(word): [
 #           w for w in words
 #           if alphabetize(w) == alphabetize(word)]
 #       for word in words}
    
    anagrams2 = {}
    for word in words:
        anagrams2.setdefault("".join(sorted(word)), [])
    for word in words:
        vari = "".join(sorted(word))
        if vari in anagrams2:
            anagrams2[vari].append(word)
    return anagrams2

the_file = 'words/short.txt'

@profile
def main(args):
    # run find_anagrams() on first argument filename
    #if len(args) < 1:
    #    print("Please specify a word file!")
    #    sys.exit(1)

    with open(the_file) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print(f"{k} : {v}")


if __name__ == "__main__":
    main()
