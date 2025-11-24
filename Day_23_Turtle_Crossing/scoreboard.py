from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 230)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def get_level(self):
        return self.level

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        return self.level

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)