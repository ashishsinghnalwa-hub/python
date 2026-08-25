fo = open("fi.txt")
l = fo.readline()
c=0
while l:
    li = l.split()
    for w in li:
        if w[0]=="t" or w[0]=="T":
            c+1
            l = fo.readline()
print(c)
