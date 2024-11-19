print("Select your ride :")
print("1. bike")
print("2. car")

#Take input from number 1 or 2
#select your ride
choice = int(input("Enter your choice :"))

#User enter option 1
if (choice == 1): #condition 1 outer if statement
 print("What type of bike?")
 print("1.scooty/n")
 print("2.scooter/n")

 #Condition for choosing type of bike
 choice2=int(input("Enter your choice2 :"))
 if choice2==1: #inner if statement
    print("You have selected scooty")
  else:
    print("You have selected scooter")

#User entering option 2
