def right():
    turn_left()
    turn_left()
    turn_left()


def left():
    turn_left()


def jump():
    left()
    move()
    right()
    move()
    right()
    move()
    left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

