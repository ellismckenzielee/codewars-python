#help bob count letters and digits kata
#https://www.codewars.com/kata/5738f5ea9545204cec000155

import re
def count_letters_and_digits(s):
    return len(re.findall('[a-zA-Z0-9]', s))
