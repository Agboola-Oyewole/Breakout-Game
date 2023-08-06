from turtle import Turtle

START_POSITION = [(-10, -260), (-10, -260)]
MOVE_DISTANCE = 50

LEFT = 180
RIGHT = 0


class Paddles:
    """Creates a new snakes and directs it forward"""

    def __init__(self):
        self.segments = []
        self.moving = True
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=1, stretch_len=9)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segments(self.segments[-1].position())

    def left(self):
        """Changes the direction of the snake left"""
        for seg in self.segments:
            seg.setheading(LEFT)
            seg.forward(MOVE_DISTANCE)

    def right(self):
        """Changes the direction of the snake right"""
        for seg in self.segments:
            seg.setheading(RIGHT)
            seg.forward(MOVE_DISTANCE)

    def not_moving(self):
        pass




