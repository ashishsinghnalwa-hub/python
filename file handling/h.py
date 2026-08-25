fr = open("f1.txt")
fw = open("f11.txt","w")
l = fr.readline()
while l:
    if l.startswith('t'):
        fw.write(l)
    l = fw.readline()
fr.close()
fw.close()