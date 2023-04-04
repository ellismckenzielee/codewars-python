# Between Extremes kata
# https://www.codewars.com/kata/56d19b2ac05aed1a20000430/train/python

def between_extremes(numbers):
    numbers.sort()
    return numbers[-1] - numbers[0]
