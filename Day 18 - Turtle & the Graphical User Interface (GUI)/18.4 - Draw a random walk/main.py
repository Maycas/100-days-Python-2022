import random
from turtle import Turtle, Screen

STEPS = 200
SPEED = 8
STEP_LENGTH = 30
PEN_WIDTH = 20
DIRECTIONS = [0, 90, 180, 270]


def get_random_color():
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    return r, g, b


tim = Turtle()
tim.speed(SPEED)
tim.pensize(PEN_WIDTH)

for _ in range(STEPS):
    color = get_random_color()
    angle = random.choice(DIRECTIONS)

    tim.forward(STEP_LENGTH)
    tim.pencolor(color)
    tim.setheading(angle)

screen = Screen()
screen.exitonclick()
