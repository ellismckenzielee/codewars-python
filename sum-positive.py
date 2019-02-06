def positive_sum(arr):
    '''Return the sum of the positive numbers'''
    total = 0
    for num in arr:
        if num > 0:
            total = total + num
    
    return total