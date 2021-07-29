#highest and lowest kata
#https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    numbers = list(map(int, numbers.split(' ')))
    return '{} {}'.format(max(numbers), min(numbers))