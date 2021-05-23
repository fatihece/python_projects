"""
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation.
"""

import string
def is_pangram(s):
    s = s.lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))