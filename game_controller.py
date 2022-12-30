from  buildhat import  Motor
from signal import pause
motor_left = Motor('A')


def moved_left(motor_speed, motor_pos, motor_apos):
    print(motor_apos)

motor_left.when_rotated = moved_left
pause()