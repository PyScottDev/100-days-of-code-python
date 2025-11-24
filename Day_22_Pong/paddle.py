from turtle import Turtle
PADDLE_SPEED = 30

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.goto(self.xcor(), new_y)

    
