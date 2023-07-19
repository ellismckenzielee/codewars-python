# Traverse Array Elements Diagonally kata
# https://www.codewars.com/kata/5968fb556875980bd900000f/train/python

def diagonal(ar):
    output = []
    for row in range(len(ar)-1, -1, -1):
        output.extend(get_row(ar, row, len(ar)-1))
    for col in range(len(ar)-2, -1, -1):
        output.extend(get_row(ar, 0, col))

    return output
    
def get_row(ar, row, col):
    vals = [];
    while (row  < len(ar) and col >= 0):
        vals.append(ar[row][col])
        row+=1
        col-=1
    return vals
        
    
    
