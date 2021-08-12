#find the first non-consecutive number kata
#https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

def first_non_consecutive(arr):
    for i, num in enumerate(arr[1:]):
        if arr[i] != num-1:
            return num
        
        