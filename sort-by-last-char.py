###Sort by last char - codewars kata
###https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0

def last(x):
    '''Return x but with elements sorted by last character'''
   x_list = (x.split(' '))
   x_list.sort(key=lambda x:x[-1])
   return x_list