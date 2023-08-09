import random
import turtle as turtle_module

import colorgram

N_COLORS = 30
DOT_SIZE = 20
STEP_SIZE = 50
N_DOTS = 100
DOTS_PER_ROW = 10


def extract_colors(image_name, n_colors):
    colors = colorgram.extract(image_name, n_colors)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors[4:]  # Filtering out whites and greys


color_list = extract_colors('hirst.jpg', N_COLORS)

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# set the pointer at the lower left corner to give space to the painting
tim.setheading(215)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, N_DOTS + 1):
    tim.dot(DOT_SIZE, random.choice(color_list))
    tim.forward(STEP_SIZE)

    if dot_count % DOTS_PER_ROW == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(DOTS_PER_ROW * STEP_SIZE)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
