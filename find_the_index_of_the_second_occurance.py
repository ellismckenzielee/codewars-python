# Find the index of the second occurance of a letter in a string kata
# https://www.codewars.com/kata/63f96036b15a210058300ca9/train/python

def second_symbol(s, symbol, count=0):
    for index, char in enumerate(s):
        if char == symbol:
            count += 1
            if count == 2:
                return index
    return -1
