#convert string to camel case kata
#https://www.codewars.com/kata/517abf86da9663f1d2000003

import re
def to_camel_case(text): 
    p = re.sub('[_-]\w', lambda x: x.group()[-1:].upper(), text)
    return p