"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join("", "dictionary_m_words.txt")
urllib.request.urlretrieve("http://bit.ly/2Cbj6zn", DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def word_cleaner(word):
    for c in word:
        if not c.isalnum():
            word = word.replace(c, "")
    return word.lower().strip()


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    cleaned_word = word_cleaner(word)
    return cleaned_word[::-1] == cleaned_word


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    words = words or load_dictionary()
    return max((word for word in words if is_palindrome(word)), key=len)
