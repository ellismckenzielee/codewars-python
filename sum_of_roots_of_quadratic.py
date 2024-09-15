# Find the sum of roots of a quadratic equation
# https://www.codewars.com/kata/57d448c6ba30875437000138

import math
def roots(a,b,c):
    try:
        one = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        two = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        return round(one + two, 2)
    except: 
        None
