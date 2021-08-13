#regexp basics - is it a vowel? kata
#https://www.codewars.com/kata/567bed99ee3451292c000025

import re
def is_vowel(s): 
    vowel = re.findall('^[aeiou]\Z', s.lower())
    return True if vowel else False