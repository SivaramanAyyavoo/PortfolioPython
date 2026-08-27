print("Hello user! Let's check if you are eligible to study our course.")
age = int(input("Please enter your age: "))

if age < 18:
    waiting_years = 18 - age
    print("Thank you for your interest. Our program eligibility is greater than 18 years old.")
    print("Please try again after", waiting_years, "years.")

if age > 18:
    print("Congrats! You are eligible to enroll the program.")

print("All the best for your learning journey!")