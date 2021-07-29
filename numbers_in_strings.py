#numbers in strings kata
#https://www.codewars.com/kata/59dd2c38f703c4ae5e000014

import re
def solve(s):
    nums = re.findall('[\d]+', s)
    nums = list(map(int, nums))
    return max(nums)