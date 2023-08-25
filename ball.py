from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_t_b(self):
        self.y_move *= -1

    def bounce_r_l(self):
        self.x_move *= -1

    def bounce_from_paddle(self):
        self.y_move *= -1

    def reset_position(self):
        self.speed('fastest')
        self.goto(0.0, -180.0)
