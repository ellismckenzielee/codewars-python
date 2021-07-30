#consecutive letters kata
#https://www.codewars.com/kata/5ce6728c939bf80029988b57

def solve(st):
    return ''.join(sorted(list(st))) in 'abcdefghijklmnopqrstuvwxyz'