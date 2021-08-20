#factorial kata
#https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc

def factorial(n):
    total = 1
    if n < 0 or n > 12:
        raise ValueError('Value Error')
    else:
        for num in range(1, n+1):
            total *= num
        return total