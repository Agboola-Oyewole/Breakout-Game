from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level_score = 1
        self.l_score = 0
        self.lives = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 230)
        self.write(f'Lives: {self.lives}  |  Score: {self.l_score}', align="center",
                   font=("Courier", 20, "normal"))

    def red_point(self):
        self.l_score += 7
        self.update_scoreboard()

    def blue_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def yellow_point(self):
        self.l_score += 4
        self.update_scoreboard()

    def level_up(self):
        self.level_score += 1
        self.update_scoreboard()

    def count_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over, Your Score is {self.l_score}', align="center", font=("Courier", 20, "normal"))

    def game_won(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'You won!, Your Score is {self.l_score}', align="center", font=("Courier", 20, "normal"))
