"""
Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char
"""
sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 1
    else:
        characters[i] += 1

keys = list(characters.keys())
best_char = keys[0]
for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key

print(best_char)