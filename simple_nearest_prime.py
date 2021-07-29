#simple nearest prime kata
#https://www.codewars.com/kata/5a9078e24a6b340b340000b8

import math
def isPrime(num):
    if (num <= 1):
            return False
    if num == 2:
        return False
    if num > 2 and num % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(num))
    for i in range(3,1+max_div, 2):
        if (num % i) == 0:
            return False
    return True
    
def solve(n):
    if isPrime(n):
        return n
    lower_num = False
    upper_num = n
    num = n
    while lower_num == False:
        num -= 1
        upper_num += 1
        if isPrime(num) == True:
            lower_num = num
            return lower_num
        if isPrime(upper_num) == True:
            return upper_num
        