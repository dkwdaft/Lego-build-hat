from turtle import Screen, Turtle
from time import sleep
from buildhat import Motor

motor_left = Motor('A')

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


ball.speed_x = 0.4
ball.speed_y = 0.4

pos_left = 0

def moved_left(motor_speed, motor_pos, motor_apos):
    global pos_left
    pos_left = motor_apos

motor_left.when_rotated = moved_left

while True:
    game_area.update()
    ball.setx(ball.xcor() + ball.speed_x)
    ball.sety(ball.ycor() + ball.speed_y)
    if ball.ycor() > 160:
        ball.speed_y *= -1
    if ball.xcor() > 195:
        ball.speed_x *= -1
    if ball.xcor() < -160:
        ball.speed_x *= -1
    paddle_left.sety(pos_left)
