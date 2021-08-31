#find multiples of a number kata
#https://www.codewars.com/kata/58ca658cc0d6401f2700045f

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))