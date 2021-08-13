#minimum to multiple kata
#https://www.codewars.com/kata/5e030f77cec18900322c535d

def minimum(a, x):
    return min(a % x, ((a // x) + 1)*x - a)