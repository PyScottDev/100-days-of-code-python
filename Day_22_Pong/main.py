from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(1200, 800)
screen.title("Pong")
screen.tracer(0)

p1 = Paddle((-550, 0))
p2 = Paddle((550, 0))
ball = Ball()

#screen.update()

screen.listen()
screen.onkeypress(p1.up, "w")
screen.onkeypress(p1.down, "s")
screen.onkeypress(p2.up, "Up")
screen.onkeypress(p2.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    if ball.wall_detect():
        ball.bounce_y()
    if ball.distance(p1) < 50 and ball.xcor() < -530:
        ball.bounce_x()
    if ball.distance(p2) < 50 and ball.xcor() > 530:
        ball.bounce_x()
 











screen.exitonclick()
