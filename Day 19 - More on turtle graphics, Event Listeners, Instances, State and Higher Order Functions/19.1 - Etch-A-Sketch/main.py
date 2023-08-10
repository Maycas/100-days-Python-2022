import turtle

STEP_LENGTH = 10
TURN_ANGLE = 10


def move_forward():
    tim.forward(STEP_LENGTH)


def turn_right():
    tim.right(TURN_ANGLE)


def turn_left():
    tim.left(TURN_ANGLE)


def move_back():
    tim.back(STEP_LENGTH)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim = turtle.Turtle()
screen = turtle.Screen()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
