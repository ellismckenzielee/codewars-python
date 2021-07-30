#diagonals sum kata
#https://www.codewars.com/kata/5592fc599a7f40adac0000a8

def sum_diagonals(matrix):
    total = 0 
    range_vals = list(range(0, len(matrix)))
    for i, j in list(zip(range_vals, range_vals[::-1])):
        total += matrix[i][i] + matrix [j][i]
    return total  