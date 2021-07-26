#stones on the table kata
#https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a

import re
def solution(stones):
    output = 0 
    for letter in 'RGB':
        matches = re.findall(rf'{letter}+', stones)
        for match in matches:
            output += len(match)-1
    return output
    