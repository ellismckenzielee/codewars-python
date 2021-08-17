#errors: histogram kata
#https://www.codewars.com/kata/59f44c7bd4b36946fd000052

import numpy as np
def hist(s):
    '''Builds upon printing error kata. Returns a histogram of the errors in:
        -Type of error
        -Error counts
        -Error count in starts
        format.'''


    unique, counts = np.unique(print_list, return_counts=True)
    dictionary_counts = dict(zip(unique, counts))
    output_string = ''
    for letter in ['u', 'w', 'x', 'z']:
        try:
            stars = dictionary_counts[letter] * '*'
            if dictionary_counts[letter] >= 10:
                space = '    '
            else: 
                space = '     '
            output_string = output_string + letter + '  ' + str(dictionary_counts[letter]) + space + stars + '\r' 
        except:
            pass
    return output_string[:-1]
