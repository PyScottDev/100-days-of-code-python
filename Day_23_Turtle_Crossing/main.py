import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

car_counter = 0
for _ in range(10):
    car.car_setup()

game_is_on = True
while game_is_on:
    car_counter += 1
    time.sleep(0.1)
    screen.update()
    
    if car_counter % 10 == 0:
        car.new_car()
    car.car_move(scoreboard.get_level())
    for car_obj in car.car_list:
        if player.distance(car_obj) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.has_reached_goal():
        player.restart()
        scoreboard.level_up()

screen.exitonclick()
