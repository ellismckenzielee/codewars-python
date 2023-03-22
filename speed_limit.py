# Speed Limit kata
# https://www.codewars.com/kata/635a7827bafe03708e3e1db6/train/python

def speed_limit(speed, signals):
    total_fine = 0
    for signal in signals:
        total_fine = total_fine + calculate_fine(speed, signal)
    return total_fine

def calculate_fine(speed, speed_limit):
    fine = 0
    if speed - speed_limit >= 30:
        fine = 500
    elif speed - speed_limit >= 20:
        fine = 250
    elif speed - speed_limit >= 10:
        fine = 100
    return fine
