#basic math (add or subtract) kata
#https://www.codewars.com/kata/5809b62808ad92e31b000031

import re
def calculate(s):
    s = re.sub('plus', '+', s)
    s = re.sub('minus','-', s) 
    return str(eval(s))