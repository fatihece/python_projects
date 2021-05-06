strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
anag = {}
for i in strs:
    element = "".join(sorted(i))
    if element in anag:
        anag[element].append(i)
    else:
        anag[element] = [i]
print(list(anag.values()))
