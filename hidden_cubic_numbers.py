#hidden cubic numbers kata
#https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python/61223ef346c17200112a766d

import re
def check_cubic(match):
    match_int = int(match)
    match = sum(list(map(lambda x: int(x)**3, list(match))))
    return (match == match_int, match_int) 

def is_sum_of_cubes(s):
    matches = re.findall('[0-9]{1,3}', s)
    output , total = '', 0
    for match in matches:
        res, num = check_cubic(match)
        if res:
            output += match + ' '
            total += num
    if output:
        return output + str(total) + ' Lucky'
    return 'Unlucky'