from turtle import Turtle

WIDTH = 400
HEIGHT = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.width = WIDTH
        self.height = HEIGHT
        self.color("orange")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
