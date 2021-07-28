#check that the situation is correct kata
#https://www.codewars.com/kata/5f78635e51f6bc003362c7d9

def check_win(lst, param):
    if all(x == param for x in lst):
        return 1
    else:
        return 0
    
def win_counter(field, param):
    wins = 0
    wins += check_win([field[0], field[4], field[8]], param)   
    wins += check_win([field[2], field[4], field[6]], param)
 
    for i in [0,3,6]:
        wins += check_win(field[i:i+3], param)
         
    for i in [0, 1, 2]:
        wins += check_win(field[i::3], param)

    return wins

def is_it_possible(field):
    x_counts = 0
    o_counts = 0
    for char in field:
        if char == 'X':
            x_counts += 1
        elif char == '0':
            o_counts += 1
    x_wins = win_counter(field, 'X')
    o_wins = win_counter(field, '0')
    if x_wins and o_wins:
        return False
    if x_wins and (x_counts - o_counts != 1):
        return False
    if o_wins and (x_counts != o_counts):
        return False
    if x_counts - o_counts not in [1,0]:
        return False
    return True
    
    
    