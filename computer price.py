class Computer:
    def __init__(self):
       self.__maxprice = 900

    def sell(self):
        print("the selling Price of the computer is", self.__maxprice)

    def setmaxprice(self,price): #setter function
        self.__maxprice = price

ob1 = Computer()
ob1.sell()

