#summing a number's digits kata
#https://www.codewars.com/kata/52f3149496de55aded000410

import re
def sum_digits(number):
    digits = re.findall('\d', str(number))
    return sum(list((map(int,digits))))