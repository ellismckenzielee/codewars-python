#happy birthday kata
#https://www.codewars.com/kata/5d65fbdfb96e1800282b5ee0/solutions/python

def wrap(height, width, length):
    dim = sorted([height, width, length])
    return 20 + dim[0]*4 + (dim[1]+dim[2]) * 2