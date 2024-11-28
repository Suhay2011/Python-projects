#Take input 
print("Half Pyramid Pattern of stars  (*):")
n = int(input("enter the number of  rows"))
#outer loop to handle number of rows
for i in range (n):
    #inner loop to handle number of columns
    for j in range (i+1):
        #display the result
        print("*" , end="")
    print()