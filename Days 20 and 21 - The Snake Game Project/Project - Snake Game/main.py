from game import Game

CANVAS_SIZE = 600
REFRESH_TIME = 0.1

new_game = Game(canvas_size=CANVAS_SIZE,
                screen_refresh_time=REFRESH_TIME)

new_game.run()
