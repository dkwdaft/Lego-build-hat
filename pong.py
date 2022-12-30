from turtle import  Screen, Turtle
from  time import sleep
from  buildhat import  Motor

game_area = Screen()
game_area.title("POONG")
game_area.bgcolor("black")
game_area.tracer(0)
game_area.setworldcoordinates(-200, -170, 200, 170)
while True:
    game_area.update()
