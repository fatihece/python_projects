""" Define a function to take a word and return negative meaning.
 Given a word, return a new word where "not " has been added to the front. 
 However, if the word already begins with "not", return the string unchanged. """



def not_string(word):
  if word.startswith('not'):
    return word
  else:
    return "not " + word

print(not_string('not bad'))
print(not_string('sugar'))
print(not_string('x'))