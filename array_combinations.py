#array combinations kata
#https://www.codewars.com/kata/59e66e48fc3c499ec5000103

def solve(arr):
    total = 1
    for array in arr:
        total *= len(set(array))
    return total