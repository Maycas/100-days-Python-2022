def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
number_of_hurdles = 6
for hurdle in range(number_of_hurdles):
    jump()
