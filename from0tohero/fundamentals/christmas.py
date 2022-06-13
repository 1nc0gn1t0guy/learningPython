picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = "*"
empty = " "

for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end=" ")
        else:
            print(empty, end=" ") # With the end = " " we are telling the interpreter to print a space instead of \n (which is the default)

    print(" ") # Because we want a new line, and python adds \n at the end of each print
    