import random

# Dictionary is like and object which store key value pair

# Generating random number by computer


user_data_match = {
        "s" : -1,
        "w" : 0,
        "g" : 1,
        "e" : 2
    }
computer_data = {
        -1 : "Snake",
        0 : "Water",
        1 : "Gun",
        2 : "Exit"
    }


while(True):

    user_input = input('''Choose One:
                        Press S for Snake: 
                        Press W for Water:
                        Press G for Gun: 
                        Press E for Exit: ''').strip().lower()
    
    if user_input not in user_data_match:
        print("Invalid input! Please enter S, W, G, or E.")
        continue

    user_input_number = user_data_match[user_input]

    computer_random_number = random.choice([-1, 0, 1])
    computer_input_number = computer_random_number

    if(user_input_number == 2):
        break

    else:
        print(f"Computer Random Number: {computer_random_number}")
        print(f"User Input Number: {user_input_number}")
        print(f"Computer Select: {computer_data[computer_input_number]} ")
        print(f"You Select: {computer_data[user_input_number]} ")

        if(user_input_number == computer_input_number):
            print("Its a Draw!!!")

        elif((computer_input_number == -1 and user_input_number == 0) or (computer_input_number == 0 and user_input_number == 1) 
            or (computer_input_number == 1 and user_input_number == -1)):
                print("You Loose: ")
        else:
            print("You Win: ")

        
