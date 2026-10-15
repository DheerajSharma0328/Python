# A tuple is a built-in data collection type used to store multiple items in a single variable. 
# Unlike lists, tuples are immutable, meaning their elements cannot be changed, added, or removed after the tuple is created.


# Empty tuple
emp = ()

# Tuple with only one item
tupone = (1,)

tup = (2,3,5,7,2,4,7,8,21,7.1,6,7,3,2)

# count is used to get occurance of a element inside a tuple
print("Count , Occurance: " , tup.count(2))

# index is used to get occurance of a element it return the index of the first element
print("Index: " , tup.index(7))
