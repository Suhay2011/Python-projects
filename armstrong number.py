# take input from user
num = int(input("Enter a number :"))

#initilise sum
sum = 0


# find the sum ofthe cube for each digit
temp = num
while temp  > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10

#display the result
if num == sum:
    print(num ,"Is eaquil to sum")
else:
    print(num ,"Is not equil to sum")