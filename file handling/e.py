fo = open("f1.txt")
l = fo.readline()
print(l.rstrip())
c = 0
while l:
    c+=1
    l=fo.readline()
    print(l,end="")
print("total no. of lines : ",c)