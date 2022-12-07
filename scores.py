from snake import SCREEN_BOUNDARIES
from turtle import Turtle
ALIGNMENT = 'center'
FONT = 'COURIER'
TYPE = 'normal'
SIZE = 24

class Score(Turtle):
    score = 0
    def __init__(self):
        print("inside score init")
        super().__init__()
        scorex = 0
        scorey = 0
        self.score = 0
        self.color('white')
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.penup()
        self.scorex = SCREEN_BOUNDARIES[1][0] - 100
        self.scorey = SCREEN_BOUNDARIES[1][1] - 40
        self.goto(self.scorex, self.scorey)
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = (FONT, SIZE, TYPE))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align = ALIGNMENT, font = (FONT, SIZE, TYPE))