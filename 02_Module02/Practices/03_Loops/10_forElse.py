passengers = ["Siva", "Raman", "Abdul", "Sree", "Gerald", "Ram", "Jhalal"]

search = input("Please enter the passenger name to search: ")

for passenger in passengers:
    if passenger == search:         # use lower()/upper() function with variables to search without case sensitive
        print("Passenger found!")
        break

else:
    print("Passenger not found!")
