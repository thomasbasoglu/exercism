"""This program checks if a sentence is a panagram"""
import string

def is_pangram(sentence):
    # Lowercase alphabet
    alphabet = set(string.ascii_lowercase)

    sentence_letters = set(sentence.lower())

    return alphabet.issubset(sentence_letters)