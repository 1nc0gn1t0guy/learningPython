from sys import argv
# read the WYSS section for how to run this

#If we want to ask for input in the command line instead of while running the program, we use argv, if not, input()
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)