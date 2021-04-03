from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"level: {self.level}", align = "left", font = FONT)

    def game_over(self):
        self.home()
        self.write(f"G A M E   O V E R", align = "center", font = FONT)
