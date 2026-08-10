import string
"""This program checks if a sentence is a panagram"""
def is_pangram(sentence):
    # Lowercase alphabet
    alphabet = set(string.ascii_lowercase)

    sentence_letters = set(sentence.lower())

    return alphabet.issubset(sentence_letters)

