library = ["section1","section2","section3"]
print("\nlibrary",library)
section1 = ["art","nature"]
section2 = ["maths","science"]
section3 = ["sst","history"]
print("\nsection1",section1)
print("\nsection2",section2)
print("\nsection3",section3)
library.remove("section1")
print("\nlibrary",library)
location = {"country": "India","state": "H.P"}
print("\nlocation",location)
section2.append("maths")
print("\nsection2",section2)
section3.reverse()
print("\nsection3",section3)
section3.sort()
print("\nsection3",section3)
visited = ["alice","bob"]
books = ["2","15"]
combined = list(zip(visited,books))
print(combined)