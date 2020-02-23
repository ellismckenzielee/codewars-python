###Take a Ten Minute Walk - codewars kata
###https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    '''Returns whether a walk is equal to 10 minuts based on directions travelled
    and number of increments'''
    north_south =  walk.count('n') == walk.count('s') 
    east_west =  walk.count('e') == walk.count('w')
    length = len(walk) == 10
    return north_south and east_west and length