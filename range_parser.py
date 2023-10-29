# Range Parser kata
# https://www.codewars.com/kata/57d307fb9d84633c5100007a/train/python

from enum import Enum
import re

class ArgType(Enum):
    RANGE_JUMP = 0
    RANGE = 1
    INT = 2
    
def range_parser(s):
    args = s.replace(' ', '').split(',')
    integers = []
    for arg in args:
        print(arg)
        arg_type = parse_type(arg)
        ints_to_append = []
        if arg_type == ArgType.RANGE_JUMP:
            start = int(re.search("^[0-9]+", arg).group())
            end = int(re.search("(?<=-)[0-9]+(?=:)", arg).group()) + 1
            step = int(re.search("[0-9]+$", arg).group())
            integers.extend(range(start, end, step))
        if arg_type == ArgType.RANGE:
            start = int(re.search("^[0-9]+", arg).group())
            end = int(re.search("(?<=-)[0-9]+$", arg).group()) + 1
            integers.extend(range(start, end))
        if arg_type == ArgType.INT:
            integers.append(int(arg))
    return integers

def parse_type(arg):
    if ':' in arg:
        return ArgType.RANGE_JUMP
    if "-" in arg:
        return ArgType.RANGE
    return ArgType.INT
