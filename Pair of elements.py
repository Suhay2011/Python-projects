# create a class
class pair_elements:

    def twoSum(self , nums , target):
        # create an empty dictionary
        Lookup = {}

        # Iterate through the touple
        for i, num in enumerate(nums):
            if target - num in Lookup:
                    return (Lookup[target - num] , i)
            Lookup[num] = i

#Take input of dum from the user
value = int(input("Enter sum of which you want to make this search :"))
print("index1=%d , index2=%d" %
pair_elements().twoSum((10,20,30,40,50,60,70),value))