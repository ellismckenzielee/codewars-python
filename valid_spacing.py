#valid spacing kata
#https://www.codewars.com/kata/5f77d62851f6bc0033616bd8

import re

def valid_spacing(s):
    for resp in [re.findall('^ ',s), re.findall('  ', s), re.findall(' $', s)]:
        if resp:
            return False
    return True
