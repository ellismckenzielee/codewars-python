###Check Free Urinals - Codewars Kata
###Given an input string, return how many free urinals there are based
### on the rules of the kata

import re
def get_free_urinals(urinals):
    ###Check for '11' error in urinals
    matches = re.findall('11', urinals)
    if matches:
        return -1
    previous_count = urinals.count('1')
    urinals = list(urinals)
    for i, urinal in enumerate(urinals):
        if i == 0:
            if len(urinals) == 1:
                return 1 - int(urinals[0])
            elif urinal =='0' and urinals[i+1] == '0':
                urinals[i] = '1'
        elif i == len(urinals)-1:
            if urinal == '0' and urinals[i-1] == '0':
                urinals[i] = '1'          
        else:
            if urinal == '0' and urinals[i-1] =='0' and urinals[i+1] == '0':
                urinals[i] = '1'
    return urinals.count('1') - previous_count