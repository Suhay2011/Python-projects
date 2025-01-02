#Initialize dictionary
test_dict = {'Codingal' : 2,'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
# printing origonal dictionary 
print("The Original Dictionary :" + str(test_dict))

#initilize value
k = 2

#using loop
#selective values in key dictionary
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

#printing result
print("Frequency of K is :" + str(res))