#Round by 0.5 steps kata
#https://www.codewars.com/kata/51f1342c76b586046800002a

import math
def solution(n):
    flr = math.floor(n)
    ceil = math.ceil(n)
    if n - flr < 0.25:
        return flr
    elif n - (flr + 0.5) >= 0.25:
        return ceil
    return flr+0.5