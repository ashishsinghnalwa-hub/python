fr = open("f1.txt")
fw = open("f11.txt","w")
l = fr.readline()
c=0
while l:
    c=c+1
    if c%2!=0:
        fw.write(l)
        print(l)
    l = fr.readline()
fr.close()
fw.close()
