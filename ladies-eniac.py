##THE LADIES OF ENIAC KATA
##Returns the name of people in a list of characters 

import re
def rad_ladies(name):
    letters = re.findall('[a-zA-Z  !]', name)
    return ''.join([letter.upper() for letter in letters])