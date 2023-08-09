from turtle import Turtle

tim = Turtle()
tim.speed(1)

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
