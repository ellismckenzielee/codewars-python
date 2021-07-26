#Two Joggers kata
#https://www.codewars.com/kata/5274d9d3ebc3030802000165

def nbr_of_laps(x, y):
    i = min(x,y)
    while i % x or i % y != 0:
        i += min(x,y)
    return (i / x, i/y)
        