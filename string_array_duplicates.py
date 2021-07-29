#string array duplicates kata
#https://www.codewars.com/kata/59f08f89a5e129c543000069

import re
def dup(arry):
    output = []
    for arr in arry:
        letters = re.findall("([\\w\\d])\\1*", arr)
        output.append(''.join(letters))
    return output
   
        