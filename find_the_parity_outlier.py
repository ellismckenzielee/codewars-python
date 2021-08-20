#find the parity outlier kata
#https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def add_one(x):
    return x + 1
    
def modulo_by_two(x):
    return x % 2
    
def find_outlier(integers):
    original_integers = integers
    integers = list(map(add_one, integers))
    integers = list(map(modulo_by_two, integers))
    
    if sum(integers) != 1:
        return original_integers[integers.index(0)]
    else:
        return original_integers[integers.index(1)]
    