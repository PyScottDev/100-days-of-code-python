from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.new_car()
        self.level_counter = 1

    def car_setup(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.goto(random.randint(-260, 280), random.randint(-260, 280))
        self.car_list.append(new_car)

    def new_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-260, 280))
        self.car_list.append(new_car)
       
    def car_move(self, level):
        level_multplier = level - 1
        for car_num in range (len(self.car_list)):
            new_x = self.car_list[car_num].xcor() - (STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level_multplier))
            self.car_list[car_num].goto(new_x, self.car_list[car_num].ycor())

    def speed_up(self):
        new_increment = self.level_counter * MOVE_INCREMENT
        new_move_distance = STARTING_MOVE_DISTANCE + new_increment
        for car_num in range (len(self.car_list)):
            new_x = self.car_list[car_num].xcor() - STARTING_MOVE_DISTANCE
            self.car_list[car_num].goto(new_x, self.car_list[car_num].ycor())
    
   