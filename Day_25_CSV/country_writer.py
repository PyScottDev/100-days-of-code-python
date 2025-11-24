from turtle import Turtle


class Country_writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    
    def write_country(self,country, x, y):
        self.goto(x, y)
        self.write(country,
                   align="center",
                   font=("Arial", 8, "normal"))