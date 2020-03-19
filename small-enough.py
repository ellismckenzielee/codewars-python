###No Loops 1 - Small Enough? - codewars kata
###https://www.codewars.com/kata/57cc4853fa9fc57a6a0002c2

def small_enough(a, limit): 
    '''Returns True if every element in a is smaller than
    limit'''
    return False if False in list(map(lambda elem: elem <= limit, a)) else True

def small_enough(a, limit):
    return max(a) <= limit