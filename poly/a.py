class India():
    def caital(self):
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
    def type(self):
        print("highly developed country")
obj_ind = India()
obj_us = USA()
for country in (obj_ind,obj_us):
    country.caital()
    country.lang()
    country.type()