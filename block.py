from turtle import Turtle


class Blocks:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.all_cars = []

    def create_car(self, color):
        for num in range(0, 11):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 3)
            new_car.color(color)
            new_car.goto(x=self.x, y=self.y)
            self.all_cars.append(new_car)
            self.x += 75
