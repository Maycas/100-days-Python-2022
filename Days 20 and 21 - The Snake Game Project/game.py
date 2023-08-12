import time
from turtle import Screen

from snake import Snake


def setup_screen(canvas_size, screen_color, game_title):
    screen = Screen()
    screen.setup(width=canvas_size, height=canvas_size)
    screen.bgcolor(screen_color)
    screen.title(game_title)
    screen.tracer(0)
    screen.listen()
    return screen


class Game:

    def __init__(self, canvas_size, screen_color, game_title, snake_body_segment_size,
                 snake_step_size, screen_refresh_time):
        self.screen = setup_screen(canvas_size, screen_color, game_title)
        self.screen_refresh_time = screen_refresh_time

        self.snake = Snake(snake_body_segment_size, snake_step_size)

        self.add_screen_event_listeners()

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

    def run(self):
        while self.game_is_on:
            self.refresh_screen()
            self.snake.move()

        self.screen.exitonclick()
