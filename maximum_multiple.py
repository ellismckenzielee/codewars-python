#maximum multiple kata
#https://www.codewars.com/kata/5aba780a6a176b029800041c

def max_multiple(divisor, bound):
    return bound - (bound % divisor)