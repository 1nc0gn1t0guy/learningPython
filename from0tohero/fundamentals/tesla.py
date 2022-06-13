def age_checker(age):

    """
    This function takes an int and compares it to default values
    in order to let the person drive the tesla or not
    """

    if int(age) >= 18:
        print("You can drive this car.")
    else: 
        print("Go home with your mum.")

age_checker(input("Your age please: ")) 