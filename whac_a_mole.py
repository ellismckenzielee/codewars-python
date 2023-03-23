# I guess this is a 6kyu kata #5: Whac-a-mole kata
# https://www.codewars.com/kata/57d250e55dc38e288c000081

def whac_a_mole(board):
    board = sorted([position for row in board for position in row])
    total_moles_hit = 0
    while len(board):
        if (len(board) >= 2):
            total_moles_hit += 2
            board = board[2:]
        else:
            total_moles_hit += 1
            board = board[1:]
        board = list(filter(lambda x: x!=0, map(decrement, board)))
    
        
    return total_moles_hit
        
def decrement(position):
    if position == 'x' or position == 0:
        return 0
    else:
        return position - 1
