#lottery machine kata
#https://www.codewars.com/kata/5832db03d5bafb7d96000107

import re
def lottery(s):
    matches = re.findall('[0-9]', s)
    used_nums, output = set(), []
    if not matches:
        return 'One more run!'
    for num in matches:
        if num not in used_nums:
            output.append(num)
            used_nums.add(num)
    return ''.join(output)