SPEED_LIMIT_MIN = 40
SPEED_LIMIT_MAX = 140

car_speed = int(input("Enter car speed: "))

if car_speed < SPEED_LIMIT_MIN or car_speed > SPEED_LIMIT_MAX:
    print("Warning: invalid car speed!!")