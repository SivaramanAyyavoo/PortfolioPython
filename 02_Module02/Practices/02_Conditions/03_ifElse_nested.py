user_name = input("Please enter your user name: ")
password = input("Please enter your password: ")

if user_name == "admin":
    if password == "adminPassword":
        print("Congrats! You are successfully logged-in.")
    else:
        print("Wrong password. Please check and retry.")
else:
    print("Wrong user name. Please check and retry")

print("Have a nice day!")