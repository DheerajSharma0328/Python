# def is to create function 
# sum is the function name
# a and b are parameter
# return is used to return the final result to whoever calling it 

# Step2 => num1 value store in a and num2 value store in num2
def sum(a,b):
# Then sum function add a and b and return their result at the palce where we call it
    return a+b


num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))

# Step1 => Here we are calling the function and pass num1 and num2 as the argumrnt
# Step3 => Now the sum recive the result of and store that result inside the add variable
add = sum(num1, num2)
# Step4 => Now we are printing value of add
print(f"Sum of {num1} and {num2} is: " , add)


# Default Argument

def default_argment(name , surname = "Sharma"):
    full_name = name + surname
    return full_name

user_name = input("Enter Your Name: ")
user_surname = input("Enter Your Surname: ")

user1 = default_argment(user_name, user_surname)
print(f"Full Name: {user1}")

# Default Argument only work when we do not pass the argument
user2 = default_argment(user_name)
print(f"Full Name: {user2}")


# Recursion


def factorial(num):
    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


number = int(input("Enter number for factorial: "))
result = factorial(number)

print(f"Factorial of {number} is: {result}")
