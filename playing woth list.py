L = [4,5,1,2,9,7,10,8]
print("Origonal List", L)

#Variable to store sum of
#The list
count = 0

#Finding the sum
for i in L:
    count += i

#divite the total elements by
#number of elements
avg = count/len(L)

print("sum =", count)
print("average =", avg)

#Sorting the element of the list
L.sort()

#printing the first element
print("Smallest element is :" , L[0])

#printing the last element
print("Largest element is:", L[-1])