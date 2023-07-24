#  The code in main can cause issues when Reeborg finds himself in a situation where
# there's a big space where it can always turn right. If that's the case, he will end
#  up in an infinite loop generating a square


def turn_right():
    turn_left()
    turn_left()
    turn_left()


#  To solve it we need to bring Reeborg in a position where it has a wall in the right
# hand side, so he can guide himself following the right wall
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
