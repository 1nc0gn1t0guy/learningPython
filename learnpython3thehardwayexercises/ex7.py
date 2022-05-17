# this line prints a string
print("Mary had a little lamb.")
# this line prints a string and introduces another string inside the {}, with the format
print("Its fleece was white as {}.".format('snow'))
# this line prints a string
print("And everywhere that Mary went.")
print("." * 10) #what'd that do? -> it will print . 10 times

# these lines assign strings to variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch end = ' ' at the end. try removing it to see what happens
# When we reomve the new variable end = ' ', the two lines will print in diferent lines, if we keep it, the two lines will be togehter
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)