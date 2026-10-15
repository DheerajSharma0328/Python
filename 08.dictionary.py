# It is used to store key-value pair
# It is unorderd
# It is mutable
# It is indexed
# Cannot store duplicate keys

mark = {
    "std1" : 90,
    "std2" : 91,
    "std3" : 92,
    "std4" : 93,
    "std5" : 94,
}

print(mark["std2"])


# Dictionary Method

# items => It give key-value pair in the form of tuple
print("Items: " , mark.items())

# key => It return key
print("Keys: " , mark.keys()) 

# values => It return values
print("Values: " , mark.values()) 

# update => it update the existing value and is if that value is not present it add those key-value pair
mark.update({"std3" : 80 , "std6" : 100})
print("Update: " , mark)

# get => It give the value of that key but when key is not present instead of throwing error it give None
print("Get: " , mark.get("Dheeraj"))
print("Get: " , mark.get("std1"))