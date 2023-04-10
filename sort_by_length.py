# Sort By Length kata
# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

def sort_by_length(arr):
    return sorted(arr, key=lambda arr: len(arr))
