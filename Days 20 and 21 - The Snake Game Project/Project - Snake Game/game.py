import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN_COLOR = "black"
GAME_TITLE = "My Snake Game"


def setup_screen(canvas_size):
    screen = Screen()
    screen.setup(width=canvas_size, height=canvas_size)
    screen.bgcolor(SCREEN_COLOR)
    screen.title(GAME_TITLE)
    screen.tracer(0)
    screen.listen()
    return screen


class Game:

    def __init__(self, canvas_size, screen_refresh_time):
        self.screen = setup_screen(canvas_size)
        self.limit = (canvas_size / 2) - 10
        self.screen_refresh_time = screen_refresh_time

        self.snake = Snake()
        self.add_screen_event_listeners()

        self.food = Food()
        self.scoreboard = Scoreboard()

        self.game_is_on = True

    def add_screen_event_listeners(self):
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.exit, "q")

    def refresh_screen(self):
        self.screen.update()
        time.sleep(self.screen_refresh_time)

    def exit(self):
        self.game_is_on = False

    def snake_collides_with_border(self):
        snake_x = self.snake.head.xcor()
        snake_y = self.snake.head.ycor()
        return snake_x > self.limit \
            or snake_x < -self.limit \
            or snake_y > self.limit \
            or snake_y < -self.limit

    def run(self):
        while self.game_is_on:
            self.refresh_screen()
            self.snake.move()

            # Detect collision with food
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.scoreboard.increase()
                self.snake.extend()

            # Detect collision with either wall or snake tail
            if self.snake_collides_with_border() or self.snake.collision_with_tail():
                self.game_is_on = False
                self.scoreboard.game_over()

        self.screen.exitonclick()
