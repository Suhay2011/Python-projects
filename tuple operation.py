#create tuple with different data types
tuplex = ("tuple" , flase , 3,2,1)
print(tuplex)

#crate a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print (tuplex)

#counts the number of occurrences of item 50 from tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple.content(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 6, 8, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beg inning of the tuple
_slice = tuplex[:6] 
print(_slice)