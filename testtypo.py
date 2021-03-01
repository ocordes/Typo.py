#!/usr/bin/env python

from Typo import Typo

# main

dictionary = Typo("en_US")

print(dictionary.check("mispelled"))
print(dictionary.check("misspelled"))
print(dictionary.suggest("mispeling"))
