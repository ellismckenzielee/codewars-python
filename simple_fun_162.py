# Simple Fun # 162: Pairwise kata
# https://www.codewars.com/kata/58afa8185eb02ea2a7000094/train/python

def pairwise(arr, n):
    total = 0
    for index, num in enumerate(arr):
        if not isinstance(num, int):
            continue
        pair = n - num
        if pair in arr:
            pair_index = arr.index(pair) 
            if pair_index == index:
                continue
            arr[index] = 'x'
            arr[pair_index] = 'x'
            total += (pair_index + index)
    return total
