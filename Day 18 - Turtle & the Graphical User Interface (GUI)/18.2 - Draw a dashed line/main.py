from turtle import Turtle, Screen

tim = Turtle()
tim.speed(1)

for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
