# Rock Paper Scissors Infinite kata
# https://www.codewars.com/kata/62443a1ea8fca9002346d72c

def winner(choices, p1, p2):
    choices_length = len(choices)
    rng = 1 + (len(choices) - 3) // 2
    choices = choices + choices
    p1_index = choices.index(p1) + choices_length
    p2_index = choices.index(p2) + choices_length
    p1_win = p2 in choices[p1_index-rng:p1_index]
    p2_win = p1 in choices[p2_index-rng:p2_index]
    if p1_win == p2_win:
        return 'Draw!'
    elif p1_win:
        return 'Player 1 won!'
    elif p2_win:
        return 'Player 2 won!'
 
