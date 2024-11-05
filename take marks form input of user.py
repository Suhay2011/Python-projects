#Take marks from input of user
Amount = int(input("Please enter your marks"))

#calculating your marks
mark_1 = Amount//85
mark_2 = (Amount%100)//68
mark_3 = ((Amount%100)%20)//99

print("amount for mark is 85%" , mark_1)
print("amount for mark is 68%" , mark_2)
print("amount for mark is 99%" , mark_3)