fo = open("f1.txt")
l = fo.readline()
c=0
while l:
    if l.startswith("the"):
        c+=1
    l = fo.readline()
print(c)
fo.close()