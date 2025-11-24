from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)

tom = Turtle()
tom.shape("turtle")
sides = 12
direction = [0, 90, 180, 270]
tom.speed("fastest")
tom.pensize(1)


def polygon(sides):
    angle = 360 / sides
    return angle


#for _ in range(sides):
#    tom.forward(100)
 #   tom.color(((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
  #  tom.right(polygon(sides))

#for _ in range(50):
 #   tom.forward(20)
  #  tom.right(random.choice(direction))
   # tom.color(((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
for _ in range(75):
    tom.color(((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
    tom.circle(100)
    tom.right(5)




screen.exitonclick()
