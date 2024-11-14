#Take input from the student to see if they can take the exam or not
medical_cause=input("Did you have a medical cause Y or N :")
#Take input from the attendance
atten= int(input)("enter the attendance of the studant :")

#Checking user input predicting output accordingly

if medical_cause == "Y" : #checking the condition 1
  print ("You are alowed")
else:
 if atten>=75 #Checkin the condition 2
  print("Allowed")
else:
  print("Not allowed")