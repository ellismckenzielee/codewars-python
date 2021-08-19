#count the divisible numbers kata
#https://www.codewars.com/kata/55a5c82cd8e9baa49000004c

def divisible_count(x,y,k):
    return (y // k) - ((x-1) // k)