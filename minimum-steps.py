###Minimum Steps - codewars kata
###https://www.codewars.com/kata/5a91a7c5fd8c061367000002/python

def minimum_steps(numbers, value):
    '''Returns the number of operations required to add progressively larger numbers in 
    numbers, to equal value'''
    numbers = sorted(numbers)
    total = 0
    for i, num in enumerate(numbers):
        total += num
        if total >= value:
            return i