###Bouncing Balls - codewars kata
###https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncingBall(h, bounce, window):
    '''Returns how many times a person in a window could see a bouncing
    ball dropped from a height above'''
    bounces = 0
    if (bounce >= 1) or (bounce <=0) or (h <0) or (window<0) or (window==h):
        return -1
    while h > window:
        h = bounce*h
        if h > window:
            bounces += 2
    return bounces + 1