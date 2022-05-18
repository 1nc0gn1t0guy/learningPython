from sys import argv

# This line assign argv to two variables, the value of those
# variables will be asked in cmd
script, filename = argv

# this will OPEN the file we have created and assign the content to txt var
txt = open(filename)

# this is a formatted string, it will print the filename using the f""
print(f"Here's your file {filename}:")
# this line will use the .read() function in order to read the file we just opened
# and print it
print(txt.read())

# this line will print the first line if no values are inside, but if we put
# values, it will read letters
print(txt.readline(20))

txt.close

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)
# print(txt_again.read())


# txt_again.close

#page 84