###Sum of powers of 2 - codewars kata
###https://www.codewars.com/kata/5d9f95424a336600278a9632

def powers(n):
    '''Returns an array of numbers that are powers
    of two, that add to make n'''
    binary_n = bin(n)
    output = []
    for i, num in enumerate(binary_n.split('b')[1][::-1]):
        print(num)
        if num == '1':
            output.append(2**i)
    return output
