import random
from turtle import Turtle, Screen


def draw_shape(turtle, num_sides):
    turning_angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(turning_angle)


tim = Turtle()
tim.speed(6)

for shape_sides_n in range(3, 11):
    R = random.randrange(0, 256, 10) / 255
    G = random.randrange(0, 256, 10) / 255
    B = random.randrange(0, 256, 10) / 255
    tim.pencolor(R, G, B)
    draw_shape(tim, shape_sides_n)

screen = Screen()
screen.exitonclick()
