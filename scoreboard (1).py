from turtle import Turtle
from ball import Ball
FONT = ("Courier", 45, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score= 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(150, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_score_r_paddle(self):
        self.r_score += 1
        self.update_score()

    def increase_score_l_paddle(self):
        self.l_score += 1
        self.update_score()