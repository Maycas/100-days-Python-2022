from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
TEXT_COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER :(", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_score_board()
