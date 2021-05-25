"""
Write a function/functions that checks whether the sentence you get from the user is a palindrome.
(Do not consider punctuation and special characters. Only consider "alphanumeric" characters.)

"""

def is_palindrome(text):
    import string
    pali = [i for i in text.lower() if i not in string.punctuation and i != " " ]
    return pali == pali[:: -1]
         
print(is_palindrome("ey edip adana'da, pide ye!"))  