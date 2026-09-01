class India():
    def capital(self):
        print("capital of India ia new delhi")
    def lang(self):
        print("mostly everyone speaks hindi")
    def type(self):
        print("India is a diverse and devloping country")
class USA():
    def capital(self):
        print("washington D.c")
    def lang(self):
        print("mostly the population speaks english")
    def type(self):                                             #for i in range meaning of type is to define the type of country and the type of country is highly developed country
        print("highly developed country")
obj_ind = India()
obj_us = USA()
for country in (obj_ind,obj_us):
    country.capital()
    country.lang()
    country.type() 