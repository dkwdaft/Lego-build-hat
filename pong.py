from turtle import  Screen, Turtle
from  time import sleep
from  buildhat import  Motor

game_area = Screen()
game_area.title("POONG")
game_area.bgcolor("black")
game_area.tracer(0)
game_area.setworldcoordinates(-200, -170, 200, 170)
ball = Turtle()
ball.color('white')
ball.shape('circle')
ball.penup()
ball.setpos(0, 0)


paddle_left = Turtle()
paddle_left.color('green')
paddle_left.shape('square')
paddle_left.shapesize(4, 1, 1)
paddle_left.penup()
paddle_left.setpos(-190, 0)
while True:
    game_area.update()