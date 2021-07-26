#Consevutive Count kata
#https://www.codewars.com/kata/59c3e819d751df54e9000098

import re
def get_consective_items(items, key): 
    items, key = str(items), str(key)
    matches = re.findall(rf'{key}+', items)
    return max(list(map(lambda x: len(x), matches)) + [0])