class Computer:
    def __init__ (self):
       self.__maxprice = 900

    def sell(self):
        print("The selling price of the computer is", self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice = price

ob1 = Computer()
ob1.sell()

ob1.setmaxprice(1000)
ob1.sell()