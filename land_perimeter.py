# Land Perimeter kata
# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python
def land_perimeter(arr):
    total = 0
    for row_index in range(len(arr)):
        for col_index in range(len(arr[0])):
            if arr[row_index][col_index] == 'X':
                above = find(row_index, col_index, -1, 0, arr)
                below = find(row_index, col_index, 1, 0, arr)
                right = find(row_index, col_index, 0, 1, arr)
                left  = find(row_index, col_index, 0, -1, arr)
                total += (above + below + right + left)
    return 'Total land perimeter: ' +  str(total)

def find(i, j, i_inc, j_inc, arr):
    try:
        if i + i_inc < 0 or i + i_inc > len(arr):
            return 1
        if j + j_inc < 0 or j + j_inc > len(arr[0]):
            return 1
        return 0 if arr[i + i_inc][j + j_inc] == 'X' else 1
    except:
        return 1

