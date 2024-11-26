#Take 2 inputs from the user
lower = int(input("Enter a Upper Range :"))
upper = int(input("Enter a Lower Range :"))

print("Prime numbers between" ,upper, "and" , lower, "are :")
#iterate the lower unit to the upper unit
for num in range (lower,upper + 1 ):
   #all prime numbers are higher than 1
   if num > 1:
      for i in range(2, num):
            if (num % i) == 0:
              break
      else:
           print(num)