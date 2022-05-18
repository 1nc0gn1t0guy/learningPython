# In here, we assign {} characters to a variable, so we can use those
# {} for a formatted string (include values inside)
formatter = "{} {} {} {}"

# Take the formatter string defined on line 3
# Call its format function, which is similar to telling it to do a command line command named format
# Pass to format four arguments, which match up with the four {} in the formatter variable.
# The result of calling format on formatter is a new string that has the {} replaced with the four variables.
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