# List are Container to store set of values of any data type

fruits = [1 , 'apple' , 2 , 'mango' , 3 , 'banana']
print (fruits)

# Index same as String
# List are mutable

# Adding Element at the end of the list 
fruits.append('grapes')
print(fruits)

# sort is used to Sort the list in ascending order
number = [6,5,3,1,4,7,8,0]
number.sort()
print("Sort: " , number)

# reverse is used to Reverse the list
number.reverse()
print("Reversed: " , number)

# insert is used to Insert element in between at any index
fruits.insert(3 , 'mango') # First position is for index where we want to place the element and second position is for that element
print("Insert" , fruits)

# pop is used to remove element from any index
number.pop(3)
print("Pop1: " , number)
print("Pop2: " , number.pop(3))

# remove method deletes the first occurrence of a specified value from a mutable collection, such as a list or a set.
number.remove(0)
print(number)