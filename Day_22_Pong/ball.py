from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.goto(0, 0)
        self.x_move = 6
        self.y_move = 6

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_detect(self):
        return self.ycor() > 380 or self.ycor() < -380

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    