#minminmax kata
#https://www.codewars.com/kata/58d3487a643a3f6aa20000ff

def minMinMax(arr):
    arr = sorted(arr)
    return [arr[0], min([x if x not in arr else arr[-1] for x in range(arr[0]+1,arr[-1])]), arr[-1]]