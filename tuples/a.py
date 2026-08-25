student = ("arav","class=5","age=10")
print(student)
print(student[0])
print(student[-1])
x,y,z = student
print(x)
print(y)
print(z)
mon_classes = {"punjabi","music","games"}
tue_clases = {"english","hindi","games","music"}
wed_clases = {"english","sst","gk","dance"}
mon_classes.add("drama")
tue_clases.discard("games")
subs = mon_classes.union(tue_clases,wed_clases)
print(subs)
same = tue_clases.intersection(wed_clases)
print(same)
rest = tue_clases.symmetric_difference(wed_clases)
print(rest)