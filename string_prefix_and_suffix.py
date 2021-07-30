#string prefix and suffix kata
#https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1

def solve(st):
    part_1 = st[:int(len(st)/2)]
    part_2 = st[int(len(st)/2):]
    if len(part_2) > len(part_1):
        part_2 = part_2[1:]
    for i, letter in enumerate(part_1):
        if part_1 != part_2:
            part_1 = part_1[:-1]
            part_2 = part_2[1:]
        else:
            return len(part_1)
    return 0
            