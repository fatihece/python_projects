"""Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis.
You are asked to calculate the number of letters or any chars 
in the sentences entered under this project.

- takes a sentence from the user,
- counts the number of each letter of the sentence,
- collects the letters/chars as a key and the counted numbers as a value in a dictionary."""


sentence = input("Enter a sentence: ")
chardict = {}
for char in sentence:
    if char not in chardict:
        chardict[char] = 1
    else:
        chardict[char] += 1
print(chardict)            
        
