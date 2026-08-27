#console's welcome message
print("="*100)
print(" "*46, "MISSION-X")
print(" "*43,"MISSION CONTROL")
print("="*100)
print("\nMISSION CONTROL SYSTEMS ONLINE\nAWAITING MISSION PARAMETERS...\n")
enter = input("PRESS ENTER WHEN READY... " )
print("="*100)

#string inputs
mission_name = input("Please enter your mission name: ")
commander_name = input("Please enter your commander name: ")
space_craft_name = input("Please enter your space craft name: ")
launch_site = input("Please enter your launch site name: ")
destination = input("Please enter your destination name: ")

#numberic inputs
#mission_duration = input("Please enter the mission duration: ")
launch_date = int(input("Please enter the launch date: "))
current_date = int(input("Please enter the today's date: "))
crew_size = int(input("Please enter your crew size: "))
craft_fuel_capacity = int(input("Please enter your space craft fuel capacity: "))
craft_mileage = int(input("Please enter your craft's mileage per liter: "))
craft_speed = int(input("Please enter your craft's speed per hour: "))

#constants
earth_moon_distance = 3_84_400  #in kilometers; as per NASA data

enter = input("Thank you for all the details.\nPress ENTER to generate the Mission Report. ")

#mission report
print("="*100)
print(" "*46, "MISSION-X")
print(" "*43,"MISSION CONTROL")
print("="*100)

print("\nMISSION IDENTIFICATION")
print("Mission Name\t\t:", mission_name)
print("Commander\t\t:", commander_name)
print("Spacecraft\t\t:", space_craft_name)
print("Launch Site\t\t:", launch_site)
print("Destination\t\t:", destination)

print("\nFLIGHT STATUS")
print("Mission Phase\t\t:", "ON TRACK...")
print("Total Distance\t\t:", earth_moon_distance, "kilometers")
print("Distance Left\t\t:", (earth_moon_distance - ((current_date - launch_date)*24)/craft_speed), "kilometers") 
print("Travel Time\t\t:", earth_moon_distance/craft_speed, "Hours")
print("Elapsed Time\t\t:", (current_date - launch_date)*24, "Hours")
print("ETA\t\t\t:", ((earth_moon_distance - ((current_date - launch_date)*24)/craft_speed)/craft_speed), "Hours")

print("\nFUEL STATUS")
print("Capacity\t\t:", craft_fuel_capacity, "Liters")
print("Consumed\t\t:", (((current_date - launch_date)*24)/craft_speed)/craft_mileage, "Liters")
print("Remaining\t\t:", craft_fuel_capacity - (((current_date - launch_date)*24)/craft_speed)/craft_mileage, "Liters")
print("Fuel Status\t\t:", "Good.")

print("\nCREW STATUS")
print("Crew Member\t\t:", crew_size)
print("Commander\t\t:", commander_name)
print("Crew Status\t\t:", "Healthy")

print("\nMISSION ASSESSMENT")
print("Flight Status\t\t:", "On Track...")
print("Fuel Status\t\t:", "Available")
print("Mission Status\t\t:", "ON\n")

print("="*100)
