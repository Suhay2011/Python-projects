#Input a word or sentance
string = int(input("Please enter your own string :"))

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i+string2

print("/nThe Origonal String =" , string)
print("/nThe Reversed String =" , string2)