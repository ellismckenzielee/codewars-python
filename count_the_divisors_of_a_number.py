#count the divisors of a number kata
#https://www.codewars.com/kata/542c0f198e077084c0000c2e

import math
def divisors(n):
    divisor_list = set()
    i = 1
    while i < math.sqrt(n) + 1:
        if n % i == 0:
            divisor_list.add(i)
            divisor_list.add(n/i)
        i += 1
    return len(divisor_list)       