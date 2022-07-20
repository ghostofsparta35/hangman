def right():
    turn_left()
    turn_left()
    turn_left()
def left():
    turn_left()

def jump():
    move()
    left()
    move()
    right()
    move()
    right()
    move()
    left()
for i in range(6):
    jump()
num_hurdles = 6
while num_hurdles > 0 :
    jump()
    num_hurdles -= 1
    print(num_hurdles)