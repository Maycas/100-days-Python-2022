import random
from turtle import Turtle, Screen

WIDTH = 500
HEIGHT = 400
SEPARATION = 50
X_END = (WIDTH / 2) - 20
STARTING_POS = (-X_END, -120)


def create_turtle(color, y_position):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=STARTING_POS[0], y=y_position)
    return new_turtle


def create_racing_turtles(turtles_colors):
    racing_turtles = []
    y_position = STARTING_POS[1]

    for color in turtles_colors:
        new_turtle = create_turtle(color, y_position)
        y_position += SEPARATION
        racing_turtles.append(new_turtle)

    return racing_turtles


is_race_on = False
screen = Screen()
screen.setup(WIDTH, HEIGHT)

user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color (red, "
                                                          "orange, yellow, green, blue or purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = create_racing_turtles(colors)

if user_bet:
    is_race_on = True
    random_distance = random.randint(0, 10)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
