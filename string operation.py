#input word
text=(input("Enter a string : "))

#Reverse string
# using stop value as -1 to interate in reverse
revtext = text[::-1]
text = revtext

print("Reverse Of Given string is:")
print(text)