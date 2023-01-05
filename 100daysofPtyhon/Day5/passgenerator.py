import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))


password = []
mylastpass = []

for lett in range(0, nr_letters):
    password.append(random.choice(letters))

for numb in range(0, nr_numbers):
    password.append(random.choice(numbers))

for symb in range(0, nr_symbols):
    password.append(random.choice(symbols))

for position in password:
    int = random.randint(0, len(password) - 1)
    mylastpass.append(password[int])

mypass = ''.join(mylastpass)

print(f"Here is your password: {mypass}")