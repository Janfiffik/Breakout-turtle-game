# --------------IMPORTS------------------
import time
import tkinter as tk
from tkinter.font import Font
from turtle import Screen
import ball
from paddle import Paddle
from blocks import Blocks

# ---------------CONSTANT VARIABLES--------
BOTTOM = -260
TOP = 260
RIGHT = 380
LEFT = -385
WIDTH = 800
HEIGHT = 600

# ---------------FUNCTIONS---------------

# ------BLOCK COLLISION -------


def check_collision_blocks():
    global new_ball, blocks
    for block in blocks.blocks:
        if new_ball.distance(block) < 35:
            block.quantity -= 1
            if block.quantity == 0:
                block.clear()
                block.goto(3000, 3000)
                blocks.blocks.remove(block)
                new_ball.bounce_t_b()
                new_ball.move()

            if new_ball.xcor() > block.right_side:
                new_ball.bounce_r_l()
                new_ball.move()

            elif new_ball.ycor() < block.left_side:
                new_ball.bounce_r_l()
                new_ball.move()

            elif new_ball.ycor() > block.upper_side:
                new_ball.bounce_t_b()
                new_ball.move()


def gameplay():
    game_on = True
    while game_on:

        window.update()
        time.sleep(0.01)
        new_ball.move()
        check_collision_blocks()
        # ---------WALL COLLISIONS_______________
        if new_ball.ycor() > TOP:
            new_ball.bounce_t_b()

        if new_ball.ycor() < BOTTOM:
            new_ball.reset_position()
            new_ball.move()

        if new_ball.xcor() > RIGHT or new_ball.xcor() < LEFT:
            new_ball.bounce_r_l()

        # ----------------PADDLE COLLISION ------------------------
        if new_ball.distance(paddle) < 100 and new_ball.ycor() < -230:
            new_ball.bounce_from_paddle()


# ----------------WINDOW-----------------
window = Screen()
window.title("Break_out")
window.setup(width=WIDTH, height=HEIGHT)
window.bgcolor("black")

new_ball = ball.Ball()
paddle = Paddle((0, -250))
blocks = Blocks()

# ---------------BLOCK CREATE _______________________


window.listen()
window.onkey(paddle.go_right, "d")
window.onkey(paddle.go_left, "a")
window.update()

# ------START BUTTON---------
startButton = tk.Button(text="Start", command=gameplay, font=Font(size=20))
startButton.pack(pady=0, padx=0)

window.mainloop()
