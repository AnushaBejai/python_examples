counts=dict()
line=input('enter a text')
words=line.split()
print(words)
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)
