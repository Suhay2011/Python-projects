try:
    num1,num2 = eval(input("Enter 2 numbers , seperated by comma :"))
    result = num1 / num2
    print("Result is" ,result)
#using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is an error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers seperated like numbers like this 1, 2:")

except:
    print("Wrong Input")

else:
    print("No exeptions")

finally:
    print("This will excuse nomatter what")