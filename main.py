#Import necessarry Modules
from abc import ABC, abstractmethod
class ABCclass(ABC):

    def print(self,x):
        print("passed value" , x)

    @abstractmethod
    def task(self):
        print("We are in ABsclass task")

class test_class(ABsclass):
    def task(self):
        print("We are inside test_class task")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)