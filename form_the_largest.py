#form the largest kata
#https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e

def max_number(n):
    n = list(map(int, str(n)))
    n = sorted(n, reverse=True)
    n = list(map(str, n))
    return int(''.join(n))