###Codewars Kata - Number of trailing zeros of a factorial

def zeros(n):
    '''Zeros calculates the number of trailing zeroes by looking at the number of prime
    factor fives'''

    total = 0
    i = 1
    while (n > 0) and (n/(5**i) >= 1):
        total += int(n/(5**i))
        i += 1
    return total