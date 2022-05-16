# assign 10 to types_of_people
types_of_people = 10
# assign the formatted string with types_of_people var to x
x = f"There are {types_of_people} types of people."

# assign the string "binary" to var binary
binary = "binary"
# assign the string "don't" to the var do_not
do_not = "don't"
# assign the formatted string with two variables inside to the var y
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assign False (boolean) to var hilarious
hilarious = False
# assign a string to a var, with a space for a var
joke_evaluation = "Isn't that jose so funny?! {}"

# this prints the string joke_evaluation and add hilarious to the {} that was reserved
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concatenates two strings
print (w + e)