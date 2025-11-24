from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.food_position()
        
    def food_position(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x, y)
        #self.goto(random.randint(-280, 280), random.randint(-280, 280))

    
   