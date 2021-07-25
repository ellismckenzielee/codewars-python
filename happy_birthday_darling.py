#Happy Birthday, Darling! kata
#https://www.codewars.com/kata/5e96332d18ac870032eb735f

def womens_age(n):
    base = n // 2
    remainder = n % 2
    return "{}? That's just {}, in base {}!".format(n, 20 + remainder, base)