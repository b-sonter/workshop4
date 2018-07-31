import sys

with open("mbox-short.txt","r") as file:
    dropChars = "!@#$%^&()_+-={}[]|\\:;\"'<>,.?/1234567890"
    dropDict = dict([(c, '') for c in dropChars])
    dropTable = str.maketrans(dropDict)

    freq = {}

    for word in file.read().split():
        tword = word.upper().translate(dropTable)
        freq[tword] = freq.get(tword,0)+1

    for key in freq.keys():
        print(key, freq[key])
