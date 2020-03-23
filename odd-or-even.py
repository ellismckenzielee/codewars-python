###Odd or Even? - codewars kata
###https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

def odd_or_even(arr):
    '''Returns even if sum of arr is even else odd'''
    return 'even' if sum(arr) % 2 == 0 else 'odd'