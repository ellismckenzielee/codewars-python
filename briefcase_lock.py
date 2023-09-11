# Briefcase Lock kata
# https://www.codewars.com/kata/64ef24b0679cdc004d08169e/train/python

def min_turns(current, target):
    total = 0
    for i in range(4):
        current_num = int(current[i]) + 1
        target_num = int(target[i]) + 1
        diff = abs(target_num - current_num)
        if diff > 5:
            diff = 10 - diff
        total += diff
    return total
