import numpy as np
def isSolved(board):
    '''Checks to see the status of a game of tic-tac-toe'''
    board = np.array(board)
    ones = False
    twos = False
    
    for i in range(0,3):
        row = board[i,:]
        print(row)
        result = check_sum(row)
        if result == 1:
            ones = True
        elif result == 2:
            twos = True
            
    for i in range(0,3):
        column = board[:,i]
        result = check_sum(column)
        if result == 1:
            ones = True
        elif result == 2:
            twos == True
            
    diagonal1 = np.diagonal(board)
    result = check_sum(diagonal1)
    if result == 1:
        ones = True
    elif result == 2:
        twos == True
        
    diagonal2 = np.rot90(board).diagonal()
    result = check_sum(diagonal2)
    if result == 1:
        ones = True
    elif result == 2:
        twos == True
            
    print(twos)
    if ones == True and twos == True:
        return 0
    elif ones == True:
        return 1
    elif twos == True:
        return 2
    else: 
        boolean_array = board > 0
        if np.sum(boolean_array) < 9:
            return -1
        else:
            return 0
            
def check_uniform(line,total):
    if total == 3:       
        boolean_arr = (line == 1)
        summation = np.sum(boolean_arr)
        if summation == 3:
            return 1
        
    elif total == 6:
        boolean_arr = (line == 2)
        summation = np.sum(boolean_arr)
        print(summation)
        if summation == 3:
            return 2
      
def check_sum(line):
    total = np.sum(line)
    if total == 3 or total == 6:
        uniform = check_uniform(line, total)
        return uniform
    else:
        return 0