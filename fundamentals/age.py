#program to know the age of an user

birth_year = input ("what year were you born?")
current_year = input ("what year is this year?")
age = int(current_year) - int(birth_year)

print("Your age is ", str(age))

#better solution

print(f"your age is: {age}")