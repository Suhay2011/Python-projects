class myClass:
    __privatVar = 27
    def __privMeth(self):
        print("I am inside the class")

    def Hello(self):
        print("The value of private variable is", myClass.__privatVar)

ob1 = myClass()
ob1.Hello()
ob1.__privMeth()