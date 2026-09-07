class laptop():                                            #init means initializing the class
    def __init__(self):
        self.__sprice = 900
        self.asprice = 360
    def info(self):
        print("actual prize:",self.asprice)
        print("selling prize:",self.__sprice)
    def change_prize(self,a,s):
        self.asprice = a
        self.__sprice = s
o1 = laptop()
o1.info()
o1.asprice = 700
o1.__sprice = 1000
o1.info()
o1.change_prize(1500,1234)
o1.info()
/create-agent
