meal_price = float(input("Please enter the planned Biryani rate for your hotel: "))

if meal_price == 100:
    print("Your Biryani price is normal. Please fix the same.")
elif meal_price > 100:
    print("Your Biryani price is overpriced. Please reduce.")
else:
    print("Your Biryani price is underpriced. Please increase.")

print("Have a nice day!")