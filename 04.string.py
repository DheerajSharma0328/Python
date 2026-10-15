#Three Ways to write String

# Single Quotes 'Dheeraj'
# Double Quotes "Dheeraj"
# Triple Single Quotes (For Muti-Line)  => ''' Hello My Name is : 
#                                                                    Dheeraj Sharma'''

# String are immutable => It mean once we create a string we cannot chnage its letter or word
# Example => once we create a string like Appple now we cannot change this to Apple just by removing the one p we need to reassgin the 
#            whole string


# String use 0 based Indexing when we start counting from left to right but when we start counting from right to left then counting start
# from -1

name = 'dheeraj'

# How to access string

nameshort = name[0:3]
# It mean copy the string which store in name varibale start from index  0 and it index 2 (here 0 is included 3 is excluded)
# Original String remain same 
# string_name[starting_index : ending_index-1]

print("Name: " ,name) 
print("Name Short" , nameshort) 


# Access String using negative number

print("Access using negative number: " , name[-4 : -1])


# This mean start from 0 and 0 is including till number-1
# start from 0 till 3
test0 = name[:4]
test1 = name[0:4]

#Both has same Output
print("Test0: " , test0)
print("Test1: " , test1)


# This mean start from 0 and 0 is included tell length-1
test3 = name[0:]
test4 = name[0:8]

# Both has same Output
print("Test3: " , test3)
print("Test4: " , test4)


# This mean start from starting index till end-1 index and skip that particualr number after the starting idex

test5 = name[0:7:2]

print("Test5: " , test5)


# String Function
# 01. len



# Length => it give total number of letter in a string includeing white space
print("Length: " , len(name)) 

#endswith => Give True or False value (Boolean value) by comparing weather a string end with our given string or not
#         => It is case sensitive
print("Ends With: " , name.endswith("a"))

# starstwith => same as endswith difference is it compare from the start
print("Start With: " , name.startswith("a"))

#capitalize => It Convert first word first letter of a string from lower case letter to upper case
print("Capitalize: " , name.capitalize())

# find => return the index first occurance of the world or leter in string
print(name.find("a"))
print(name.find("e"))

# replace => replace the all old world with new
test6 = "hello everyone  , hello all , hello i am audible"
print(test6.replace("hello" , "Hey"))


