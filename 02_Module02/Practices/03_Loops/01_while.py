#  Repeats code while a condition is true

count_down = int(input("Please enter a number for count down to 0: "))

while count_down != -1:
    print(count_down)
    count_down -= 1     # missing this value change or value change in opposite direction will creat infitinity loop

print("Done!")
