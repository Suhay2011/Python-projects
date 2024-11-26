#Take input of a word
string = input("Enter your own word :")

#take input from character
char = input("Enter your own character :")
i = 0
count = 0
#loop will find the occurence of a character
while(i < len(string)) : #string operation

  if(string[i] == char) : #Condition 1:
   count = count +1

i = i + 1

#display the result 
print("The total number of times" ,char , "has occured =", count)