from turtle import *
from gpiozero import Buzzer
from buildhat import Motor

score_left = 0
score_right = 0

buzz = Buzzer(22)

motor_left = Motor('A')
motor_right = Motor('B')

game_area = Screen()
game_area.title('PONG')
game_area.bgcolor('black')
game_area.tracer(0)
game_area.setworldcoordinates(-200, -170, 200, 170)

ball = Turtle()
ball.color('white')
ball.shape('circle')
ball.penup()
ball.setpos(0, 0)

paddle_left = Turtle()
paddle_left.color('green')
paddle_left.shape("square")
paddle_left.shapesize(4, 1, 1)
paddle_left.penup()
paddle_left.setpos(-190, 0)

paddle_right = Turtle()
paddle_right.color('blue')
paddle_right.shape("square")
paddle_right.shapesize(4, 1, 1)
paddle_right.penup()
paddle_right.setpos(190, 0)

writer = Turtle()
writer.hideturtle()
writer.color('grey')
writer.penup()
style = ('Courier', 30, 'bold')
writer.setposition(0, 150)
writer.write(f'{score_left} PONG {score_right}', font=style, align='center')

ball.speed_x = 0.4
ball.speed_y = 0.4

pos_left = 0
pos_right = 0


def moved_left(motor_speed, motor_rpos, motor_apos):
    global pos_left
    pos_left = motor_apos


def moved_right(motor_speed, motor_rpos, motor_apos):
    global pos_right
    pos_right = motor_apos


motor_left.when_rotated = moved_left
motor_right.when_rotated = moved_right

while True:
    game_area.update()
    ball.setx(ball.xcor() + ball.speed_x)
    ball.sety(ball.ycor() + ball.speed_y)
    if ball.ycor() > 160:
        ball.speed_y *= -1

    if ball.ycor() < -160:
        ball.speed_y *= -1
    paddle_left.sety(pos_left)
    paddle_right.sety(pos_right)
    if (-180 > ball.xcor() > -190) and (
            paddle_left.ycor() + 20 > ball.ycor() > paddle_left.ycor() - 20):
        ball.setx(-180)
        ball.speed_x *= -1
        buzz.beep(0.1, 0.1, background=True)

    if(180 < ball.xcor() < 190) and (paddle_right.ycor() + 20 > ball.ycor() > paddle_right.ycor() - 20):
        ball.setx(180)
        ball.speed_x *= -1
        buzz.beep(0.1, 0.1, background=True)

    if ball.xcor() < -195:  # Left
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        score_right += 1
        buzz.beep(0.5, 0.5, background=True
        writer.clear()
        writer.write(f'{score_left} PONG {score_right}', font=style, align='center')

    if ball.xcor() > 195:  # Right
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        score_left += 1
        buzz.beep(0.5, 0.5, background=True
        writer.clear()
        writer.write(f'{score_left} PONG {score_right}', font=style, align='center')
