#using a try and accept
try:
    number = int(input("Enter a number"))
    print("The number entered is :" ,number)
#using value error
except ValueError as ex:
     print("Exeption" ,ex)