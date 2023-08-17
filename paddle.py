import random
from turtle import Turtle
#class ile çalışırken func elemanlarını self ile yazmayı unutma.

colors = ["red", "orange","green","pink","white"]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    #    self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)

    def change_color_paddle(self):
        for color in colors:
            new_color = random.choice(colors)
            self.color(new_color)







