#character with longest consecutive repetition kata
#https://www.codewars.com/kata/586d6cefbcc21eed7a001155

from itertools import groupby
def longest_repetition(chars):
    maximum = 0
    letter = ''
    split_string = ["".join(g) for k, g in groupby(chars)]
    print(split_string)
    for section in split_string:
        length = len(section)
        if length > maximum:
            letter = section[0]
            maximum = length
    return (letter, maximum)