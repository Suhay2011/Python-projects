# parent class
class Person( object ):
                
                # __init__ is known as the constructor
                def __init__(self, name, idnumber):
                    self.name = name
                    self.idnumber = idnumber
                def display(self):
                        print(self.name)
                        print(self.idnumber)

# child class
class Employee( Person ):
        def __init__(self, name, idnumber, slary, post):
               self.salary = slary
               self.post = post


               #Invoking the __init__ of the parent class
               Person.__init__(self, name, idnumber)


#creation on an object variable or an instance
a = Employee('Rahul', 886012 200000 ,"Intern")

#calling a function of a class Person using it's instance
a.display()