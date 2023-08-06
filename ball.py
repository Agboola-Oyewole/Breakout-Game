from turtle import Turtle
from random import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.level = 1
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.goto(0, -230)
        heading = choice([45, -45])
        self.setheading(heading)

    def move(self):
        if self.level == 1:
            self.fd(20)
        else:
            self.move_speed = 0.9
            self.fd(20)

    def bounce_y(self):
        self.move_speed -= 0.005
        self.setheading(-1 * self.heading())

    def paddle_corner_bounce1(self):
        if self.heading() == self.heading():
            self.setheading(-1 * self.heading())
        else:
            self.setheading((self.heading() + 180))

    def paddle_corner_bounce2(self):
        if self.heading() == self.heading():
            self.setheading((self.heading() - 180))
        else:
            self.setheading(-1 * self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
