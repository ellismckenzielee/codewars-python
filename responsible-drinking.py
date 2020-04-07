###Responsible Drinking - codewars kata
###https://www.codewars.com/kata/5aee86c5783bb432cd000018

import re
def hydrate(drink_string): 
    '''Returns number of waters to balance alcoholic drinks found 
    in drink string'''
    drink_total = sum(list(map(int,re.findall('[\d]+', drink_string))))
    
    glasses = ('glass' if drink_total == 1 else 'glasses')
    return '{} {} of water'.format(drink_total, glasses)