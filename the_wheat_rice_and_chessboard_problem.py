#the wheat/rice and chessboard problem kata
#https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7

def squares_needed(grains):
    square = 0
    ans = 1
    while ans <= grains:
        ans *= 2
        square += 1
    return square