import random
from turtle import Turtle
COLORS = ["green", "blue", "yellow", "orange", "purple", "red", "royal blue",
          'light cyan', 'sandy brown', 'deep pink', 'medium sea green', 'khaki']

LIVES = [
         1, 2, 1, 3, 2, 1, 4, 1, 3, 2,
         2, 1, 3, 1, 1, 2, 4, 1, 2, 3,
         1, 2, 1, 2, 3
         ]


class Block(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLORS))
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(LIVES)

        self.left_side = self.xcor() - 30
        self.right_side = self.xcor() + 30
        self.upper_side = self.ycor() + 15
        self.bottom_side = self.ycor() - 15


class Blocks:
    def __init__(self):
        self.y_start = 30
        self.y_end = 270
        self.blocks = []
        self.create_lanes()

    def create_lane(self, y_cor):
        for i in range(-385, 380, 63):
            block = Block(i, y_cor)
            self.blocks.append(block)

    def create_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)
