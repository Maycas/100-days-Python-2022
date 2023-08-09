import random
from turtle import Turtle, Screen

RADIUS = 100
STEPS = 50
SPEED = "fastest"
PEN_WIDTH = 3


def random_color():
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    return r, g, b


def draw_spirograph(turtle, radius, steps):
    for _ in range(steps):
        turtle.pencolor(random_color())
        turtle.circle(radius)
        turtle.right(360 / steps)


tim = Turtle()
tim.speed(SPEED)
tim.pensize(PEN_WIDTH)

draw_spirograph(tim, RADIUS, STEPS)

screen = Screen()
screen.exitonclick()
