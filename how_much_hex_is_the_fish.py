# how much hex is the fish kata
# https://www.codewars.com/kata/5714eb80e1bf814e53000c06

def fish_hex(name):
    name = name.lower()
    bitwise_or = 0
    for char in name:
        if char in "abcdef":
            bitwise_or = bitwise_or ^ int(char, 16)
    return bitwise_or
