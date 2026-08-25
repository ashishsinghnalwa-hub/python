fo = open("f1.txt")
ch = fo.read(1)
c = 0
while ch:
    if ch in ["a,e,i,o,u,A,E,I,O,u"]:
        c + 1
        ch = fo.read(1)
        print("total no. of vowels",c)