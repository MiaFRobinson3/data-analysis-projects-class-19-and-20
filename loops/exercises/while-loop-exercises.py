# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel_level = 0
num_astronauts = 0
altitude = 0

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 
while fuel_level <= 5000 or fuel_level > 30000:
    fuel_level = int(input("Enter the starting fuel level: "))

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
while num_astronauts <= 0 or num_astronauts > 7:
    num_astronauts = int(input("Enter the number of astronauts: "))
if num_astronauts < 7:
    print("Less than 7 astronauts")
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while fuel_level-100*num_astronauts >= 0:
    fuel_level -=(100*num_astronauts)
    altitude += (50)
if fuel_level >= 0:
    print("DANGER")
  
# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
if altitude >= 2000:
    ending = "Orbit Achieved!"
else:
    ending = "Failed to reach orbit"
print("The shuttle gained an altitude of", altitude, "km and has", fuel_level, "kg of fuel left.", ending)