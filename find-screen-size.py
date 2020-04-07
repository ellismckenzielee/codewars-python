###Find Screen Size - codewars kata
###https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f

def find_screen_height(width, ratio): 
    '''Finds and returns screen height based on AR and 
    width'''
    lhs, rhs = list(map(int, ratio.split(':')))
    height = int(width * rhs/lhs)
    return str(width) + 'x' + str(height)