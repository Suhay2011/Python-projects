#take input from user
rowSize = int(input("Enter the number of rows :"))
if rowSize%2==0: #conditions
    halfDiamondRow = int(rowSize/2)
else:
    halfDiamondRow = int(rowSize/2)+1
space = halfDiamondRow-1
#Loop for upper part
for i in range (1 ,halfDiamondRow+1): #loop for rows
  for j in range (1, space+1): #loop for columns
     print(end="")
  space = space-1
  num = 1
  for j in range(2*i-1):
     print(end=str(num))
  #incrementin number at each column
     num = num+1
  print()
space = 1
#loop for lowest part
for i in range (1,halfDiamondRow): #loop for rows
   for j in range (1, space+1): #loop for columns
      print(end="")
      space = space+1
      num = 1
      for j in range(1, 2*(halfDiamondRow-i)):
         print(end = str(num)) #display the result
      
      #incrementin number at each column
         num = num+1
      print()