from abc import ABC,abstractclassmethod
class animal(ABC):
    def behave(self):
        pass
class human(ABC):
    def behave(self):
        print("i can think")
class snake(ABC):
    def behave(self):
        print("i can crawl and bite")
class dog(ABC):
    def behave(self):
        print("i can bark")
class lion(ABC):
    def behave(self):
        print("king of the jungle")
o1=human()
o1.behave()
o2=snake()
o2.behave()
o3=dog()
o3.behave()
o4=lion()
o4.behave()