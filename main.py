import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
screen.update()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(player.move, "space")

game_started = True
while game_started:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect if car smacks the turtle
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_started = False

    # detect if turtle has crossed the road
    if player.successful_crossing():
        player.goto_start()
        scoreboard.level += 1
        scoreboard.display()
        car_manager.level_up()

scoreboard.game_over()

screen.exitonclick()
