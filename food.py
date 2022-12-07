from turtle import Turtle
from snake import SCREEN_BOUNDARIES
from random import randint


class Food(Turtle):
    foodx = 0
    foody = 0
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        foodx = randint(SCREEN_BOUNDARIES[0][0] - 10, SCREEN_BOUNDARIES[1][0] - 10)
        foody = randint(SCREEN_BOUNDARIES[0][1] - 10, SCREEN_BOUNDARIES[1][1] - 10)
        self.goto(foodx, foody)
        print(f"Food located at {foodx}, {foody}")

