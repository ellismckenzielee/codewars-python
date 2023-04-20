# Simple Fun #250: Prefix Sums to Suffix Sums kata
# https://www.codewars.com/kata/590c4c342ad5cd6a8700005c/train/python/64413d15abc98500651861fc

def prefix_sums_to_suffix_sums(prefix_sums):
    initial = []
    prev = 0
    for  prefix in prefix_sums:
        initial.append(prefix - prev)
        prev = prefix
    prev = sum(initial)
    suffixes = [prev]
    for num in initial[0:-1]:
        suffixes.append(prev-num)
        prev = prev-num
    return suffixes
