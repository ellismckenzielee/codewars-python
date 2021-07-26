#Status arrays kata
#https://www.codewars.com/kata/601c18c1d92283000ec86f2b

def status(nums):
    nums_with_position = []
    for i, num in enumerate(nums):
        previous_smaller = len(list(filter(lambda x: x < num, nums)))
        nums_with_position.append([previous_smaller + i + 1, i, num])
    return list(map(lambda x: x[2], sorted(nums_with_position, key=lambda x: (x[0]))))