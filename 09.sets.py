# Both Set and Dictionary is made using {}
# Set is collection of non-repetitive elements
# We can not repeat elemnet in a set 
# If we repeat the element expilicitly stll it take that element only once
# Set are unorderd
# Set are unindexed
# There is not way to change item in set
# Set canot contain duplicate values

# Empty Set
s = set()
# Set with values
se = {1,5,10}

# Empty Dictionary
d = {}

# Set Operation

data = {1,2,5,12,1,2,32,6,32,2}
print("Set: " , data)

# add

data.add(9)
print("Set: " , data)

# length
print("Length: " , len(data))

# remove 
data.remove(1)
print("1 Removed: " , data)

# pop => it remove random element from the set
print("Pop: " , data.pop())

# clear
# data.clear()
# print("Clear: " , data)



# Union <-----> Intersection

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,11,12,13,14,15}

# Union => It return a new set with all the value in both set without repeatation
print("Union: " , set1.union(set2))

# Intersection => It return common value in both the set
print("Intersection: " , set1.intersection(set2))

