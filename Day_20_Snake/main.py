from turtle import Turtle, Screen
import pygame
from snake import Snake
from food import Food
from score import Score
import time 

pygame.mixer.init()

eat_sound = pygame.mixer.Sound("Day_20_Snake/eat.wav")
game_over_sound = pygame.mixer.Sound("Day_20_Snake/game_over.wav")

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# score_writer = Turtle()
# score_writer.hideturtle()
# score_writer.penup()
# score_writer.color("white")
# score_writer.goto(0, 260)
# score_writer.write("Score: 0", align="center", font=("Arial", 24, "normal"))

snake = Snake()
food = Food()
score = Score()

screen.textinput("Ready?", "Press Enter to start the game")


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075)
    
    snake.move()
    if snake.head.distance(food) < 15:
        food.food_position()
        eat_sound.play()
        score.increase_score()
        snake.snake_grow()
    snake.wrap_screen()
    # if snake.wall_detect():
    #     game_over_sound.play()
    #     score.reset_score()
    #     snake.snake_reset()
    if snake.snake_collision():
        game_over_sound.play()
        score.reset_score()
        snake.snake_reset()



screen.exitonclick()

