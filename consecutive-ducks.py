###Consecutive Ducks - codewars kata
###https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f
import math
def consecutive_ducks(n):
    '''Returns True if number n can be expressed as the sum of two or more consecutive 
    positive numbers'''
    return not math.log(n, 2).is_integer()