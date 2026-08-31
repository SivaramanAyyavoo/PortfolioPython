secret_number = 34

user_input = int(input("Guess the secret number: "))

while user_input != secret_number:
    if user_input > secret_number:
        print("Too high.")
    else:
        print("Too low.")
    user_input = int(input("Guess the secret number: "))    # without this line, the while loop will create the endless loop

print("Congrats you found the secret number!!")

# while loop always create an infite loop till the condition is TRUE; So, we need to introduce the break code for this to avoid infinite loop