#the office VI - sabbatical kata
#https://www.codewars.com/kata/57fe50d000d05166720000b1

import re
def sabb(s, value, happiness):
    letters = re.findall('[sabatical]', s)
    return 'Sabbatical! Boom!' if len(letters) + value + happiness > 22 else 'Back to your desk, boy.'
    