#Assign 100 to cars
cars = 100
#Assign 4.0 to space_in_a_car
space_in_a_car = 4.0
#Assign 30 to drivers
drivers = 30
#assign 90 to passengers
passengers = 90
#substracts drivers to cars and assign the result to cars_not_driven
cars_not_driven = cars - drivers
#Assign drivers' value to cars_driven
cars_driven = drivers
#multiplies cars_driven to space_in_a_car and assign the value to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#Divides passengers by cars_driven and assign the value to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have,", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")