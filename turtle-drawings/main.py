import turtle
import random

# Set up the screen and turtle
t = turtle.Turtle()
t.speed(0)  # 0 is the fastest speed
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")

colors = ["red", "purple", "blue", "green", "orange", "yellow"]
random_color = random.choice(colors)

def draw_shape(side_length, num_sides):
    for _ in range(num_sides):
        t.forward(side_length)
        t.right(360 / num_sides)

# We want to call draw_shape() multiple times in a loop
for i in range(36):
    color_cycle = i % len(colors)
    random_sides = random.randint(3, 10)
    t.fillcolor(colors[color_cycle])
    t.pencolor(colors[color_cycle])
    t.begin_fill()    
    draw_shape(random.randint(50, 150), random_sides)
    t.end_fill()
    t.right(10)

screen.update()
screen.exitonclick()