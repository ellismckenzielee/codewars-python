#How many reindeers? kata
#https://www.codewars.com/kata/52ad1db4b2651f744d000394

import math
def reindeer(presents):
    total = 2 
    total += math.ceil(presents/30)
    if total <= 8:
        return total
    else:
        raise ValueError('Santa needs too many reindeers')