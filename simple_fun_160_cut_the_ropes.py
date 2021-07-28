#simple fun #160: cut the ropes kata
#https://www.codewars.com/kata/58ad388555bf4c80e800001e

def cut_the_ropes(arr):
    remaining_list = [len(arr)]

    for num in arr:
        minimum = min(arr)
        arr = list(map(lambda x: x-minimum, arr))
        remaining = len(arr) - arr.count(0)
        arr = list(filter(lambda x: x != 0, arr))
        if remaining == 0:
            return remaining_list
        remaining_list.append(remaining)
        