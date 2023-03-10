# Heron's Formula kata
# https://www.codewars.com/kata/57aa218e72292d98d500240f

import math
def heron(a, b, c):
    s = (a + b + c) / 2
    return round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
