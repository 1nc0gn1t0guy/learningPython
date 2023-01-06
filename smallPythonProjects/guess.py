from random import randint

i = randint(0, 100)
print("Adivina el numero!")
print(i)

while True:

    guess = int(input("Introduce tu eleccion!\n> "))
    
    if guess > i:
        print("Tu numero esta por encima del numero aleatorio")
    
    elif guess < i:
        print("Tu numero esta por debajo del numero aleatorio")
    
    else:
        print("Acertaste!!")
        exit()