# Switch On the Gravity kata
# https://www.codewars.com/kata/64c743cb0a2a00002856ff73

def switch_gravity(lst):
    col_items = []
    gravity_lst = [[] for row in lst]
    for column_indx in range(len(lst[0])):
        col_items.append([row[column_indx] for row in lst].count('#'))
    
    for row_indx, row in enumerate(lst):
        for column_indx, column in enumerate(row):
            if row_indx >= len(lst) - col_items[column_indx]:
                gravity_lst[row_indx].append('#')
            else:
                gravity_lst[row_indx].append('-')
    return gravity_lst
