print("Lets check your voting eligibility.")
age = int(input("Please enter your for verificaiton: "))

if age >= 18:
    print("You are eligible for voting. Please apply for voter ID.")
else:
    print("You are not eligible for voting. Please apply after", 18-age, "years.")
print("Jaihind!")