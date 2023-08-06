import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from block import Blocks
from paddles import Paddles

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddles()
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

game_is_on = True


red_blocks = Blocks(x=-360, y=180)
red_blocks.create_car(color='red')
green_blocks = Blocks(x=-360, y=140)
green_blocks.create_car(color='green')
yellow_blocks = Blocks(x=-360, y=100)
yellow_blocks.create_car(color='yellow')
blue_blocks = Blocks(x=-360, y=60)
blue_blocks.create_car(color='blue')

while game_is_on:
    if ball.move_speed <= 0.005:
        ball.move_speed = 0.005
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    for dog in paddle.segments:
        if dog.xcor() <= -340:
            dog.goto(-310, -260)

        elif dog.xcor() >= 340:
            dog.goto(310, -260)

    # detect collision with left and right wall
    if ball.xcor() >= 370 or ball.xcor() <= -380:
        ball.bounce_x()

    # detect collision with paddles
    if ball.ycor() >= -260:
        # detect collision with the left corner edge of the paddle
        if ball.ycor() < -235 and ball.distance(paddle.segments[0]) < 80:
            ball.paddle_corner_bounce1()
        # detect collision with the right corner edge of the paddle
        elif ball.ycor() < -235 and ball.distance(paddle.segments[1]) < 110:
            ball.paddle_corner_bounce2()

    # detect collision with top wall
    if ball.ycor() > 283:
        ball.bounce_y()

    # detect collision with bottom wall
    if ball.ycor() < -290:
        scoreboard.count_lives()
        ball.reset_position()
    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False
    if len(red_blocks.all_cars) == 0 and len(blue_blocks.all_cars) == 0 and len(green_blocks.all_cars) == 0 \
            and len(yellow_blocks.all_cars) == 0:
        scoreboard.game_won()
        game_is_on = False

    for car in red_blocks.all_cars:
        if car.distance(ball) < 40:
            ball.bounce_y()
            red_blocks.all_cars.remove(car)
            car.goto(10000, 10000)
            scoreboard.red_point()

    for car in green_blocks.all_cars:
        if car.distance(ball) < 40:
            ball.bounce_y()
            green_blocks.all_cars.remove(car)
            car.goto(10000, 10000)
            scoreboard.red_point()

    for car in blue_blocks.all_cars:
        if car.distance(ball) < 40:
            ball.bounce_y()
            blue_blocks\
                .all_cars.remove(car)
            car.goto(10000, 10000)
            scoreboard.blue_point()

    for car in yellow_blocks.all_cars:
        if car.distance(ball) < 40:
            ball.bounce_y()
            yellow_blocks.all_cars.remove(car)
            car.goto(10000, 10000)
            scoreboard.yellow_point()

screen.exitonclick()
