fo = open("f1.txt")
l = fo.readline()
c=0
while l:
    c=c+1
    li = l.split()
    print("line",c,"total no.",len(li))
    l = fo.readline()
fo.close()