#holiday II - plane seating kata
#https://www.codewars.com/kata/57e8f757085f7c7d6300009a

import regex as re
def plane_seat(a):
    row = int(''.join(re.findall('\d', a)))
    seat = re.findall('[A-Z]', a)[0]
    
    row_location = ''
    seat_location = ''
    if row < 21:
        row_location = 'Front'
    elif row < 41:
        row_location = 'Middle'
    elif row < 61:
        row_location = 'Back'
    else:
        return 'No Seat!!'
    
    if seat in 'ABC':
        seat_location = 'Left'
    elif seat in 'DEF':
        seat_location = 'Middle'
    elif seat in 'GHK':
        seat_location = 'Right'
    else:
        return 'No Seat!!'
    
    return row_location + '-' + seat_location
        
    
    