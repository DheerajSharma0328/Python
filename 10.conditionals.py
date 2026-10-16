# age = int(input("Enter Your Age: "))

# if(age>=18):
#     print("You are eligile for voting: ")

# elif(age<0):
#     print("Please enter postive number: ")

# else:
#     print("Your are under age can't give vote sorry!!! ")


# if(age>=18):
#     print("You can work ")

# else:
#     print("You cannot vote sorry!!! ")


# # and or not 

# # and

# num1 = int(input("Enter Number1: "))
# num2 = int(input("Enter Number2: "))
# num3 = int(input("Enter Number3: "))

# if(num1 == num2 and num3 == num1):
#     print("All Number are equal")
# else:
#     print("All number are not equal")

# if(num1 >= num2 or num1 >= num3):
#     print("Number1 is Greater than either Number 2 or Number 3")
# else:
#     print("Number1 is the smallest")

# boolean = bool(int(input("Enter either 0 or 1 ")))

# if boolean is None:
#     print("You Entered Wrong input. Enter either 0 or 1")
# elif (not boolean) : # 0=>1 1=>0
#     print("You entered False")  # If it is NOT True, it must be False
# else:
#     print("You entered True")

# print(not boolean)


str1 = "Make a lot of money"
str2 = "Buy now"
str3 = "Suscribe this"
str4 = "Click this"

message = input("Enter Your Message: ")

if((str1 in message) or (str2 in message) or (str3 in message) or (str4 in message)):
    print("This Message is a Spam")
else:
    print("Message is not a spam")
