#regexp basics - is it a digit? kata
#https://www.codewars.com/kata/567bf4f7ee34510f69000032

import re
def is_digit(n):
    match = re.findall('[\d]', n)
    return match[0] == n if match else False
    