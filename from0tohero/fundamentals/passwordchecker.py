#ask for user, password, print username, password converted to ***** and password length

username = input("Username: ")
password = input("Password: ")

password_lenght = len(password)
password_encoded = "*" * password_lenght

print(f"Hi {username}, your password {password_encoded} is {password_lenght} letters long")