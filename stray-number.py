def stray(arr):
    '''Finds the stray number in an array'''
    first_num = arr[0]
    second_num = arr[1]
    if first_num != second_num:
        third_num = arr[2]
        if third_num == second_num:
            return first_num
        else:
            return second_num
    for num in arr:
        if num != first_num:
            return num