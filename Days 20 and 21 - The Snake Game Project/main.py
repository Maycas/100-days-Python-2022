from game import Game

CANVAS_SIZE = 600
BODY_SEGMENT_SIZE = 20
STEP = 20
REFRESH_TIME = 0.1

new_game = Game(canvas_size=CANVAS_SIZE, screen_color="black", game_title="My Snake Game",
                snake_body_segment_size=BODY_SEGMENT_SIZE, snake_step_size=STEP, screen_refresh_time=REFRESH_TIME)
new_game.run()
