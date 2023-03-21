# Kids and candies kata
# https://www.codewars.com/kata/56cca888a9d0f25985000036/train/python

import math
def candies_to_buy(amount_of_kids_invited):
    lcm = 1
    for num in range(1, amount_of_kids_invited+1):
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm
