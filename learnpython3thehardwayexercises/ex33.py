def whileloop(number):
    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i += 1
        print("Numbers now: ", numbers)
        print(f"At th bottom i is {i}")

    return numbers


print("How long do you want the list to be?")
number = int(input("> "))

numbers = whileloop(number)

print("The numbers: ")

for num in numbers:
    print(num)

################################################################

numbers2 = []

for j in range(0,6):
    print(f"At the top i is {j}")
    numbers2.append(j)
    
    print("Numbers now: ", numbers2)
    print(f"At th bottom i is {j}")
