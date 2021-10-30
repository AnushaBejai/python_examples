import re
name=input('enter file:')
handle=open(name)
lst=list()
for line in handle:
    line.rstrip()

    stuff=re.findall('[0-9]+',line)
    if len(stuff)<1:
        continue


    for x in range(len(stuff)):
        num=int(stuff[x])
        lst.append(num)


print(sum(lst))
