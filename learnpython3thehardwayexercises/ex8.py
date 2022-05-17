# In here, we assign {} characters to a variable, so we can use those
# {} for a formatted string (include values inside)
formatter = "{} {} {} {}"

# With all these print lines we are introducing strings, numbers, booleans,
# and even a variable inside the {} 
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))