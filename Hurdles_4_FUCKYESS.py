def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and not right_is_clear():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()




