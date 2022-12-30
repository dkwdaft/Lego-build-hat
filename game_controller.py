from buildhat import Motor

motor_left = Motor('A')

while True:
    print(motor_left.get_aposition())