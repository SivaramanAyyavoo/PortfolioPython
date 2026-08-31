attempts = 0
user_password = "India1947"

while attempts < 3:
    password = input("Please enter your password: ")
    if password == user_password:
        print("Login Sucessful.")
        break

    attempts += 1
    print("Incorrect password. Try again.\nYou have", 3 - attempts, "more attempts to enter the correct password")

else:
    print("Login failed.\nYou have reached the maximum number of attempts for the day. Try again tomorrow.")
