def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
        turn_right()
    else:
        turn_left()


# This code is not going to work in a normal station, refer to this webpage:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json