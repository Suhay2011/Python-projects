#Assigning Different Variables
name = "penguin"
age = 15
is_student = True
weight = 38.5

#Printing Different Variables and their Data Types
print("Name :" , name)
print("Data type of Name is:" , type(name))

print("Age :", age)
print("Data type of Age is" ,type(age))

print("is_student :" , is_student)
print("is_student :" , type(is_student))

print("weight" , weight)
print("Data type of weight is:" , type(weight))

#Type casting to convert the data type of variables
print("/nAfter type Casting...")
age = str(age)
print(age)
print("Data Type of age is" ,type(age))
weight=int(weight)
print(weight)
print("Data Type of weight is:" , type(weight))