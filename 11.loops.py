# For Loop
# Here counting start from 1 mean 1 is including and continue till 10 mean 11 is excluded

# range() in Python
# It generates a sequence of integers that a loop can iterate over.
# There are three common forms:

# Syntax	                    Meaning

# range(stop)	                Starts at 0, stops before stop
# range(start,stop)	            Starts at start, stops before stop
# range(start,stop, step)	    Starts at start, stop at stop and advances(skip) by step

for i in range(1,3):
    print(i)

# While Loop

i = 1

while(i<3):
    print(i)
    i += 1


# Table

table = int(input("Enter Number: "))
i = 1

while(i<11):
    print(f"{table} * {i} => {table*i}")
    i += 1