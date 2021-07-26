#Digit recovery kata
#https://www.codewars.com/kata/5964d7e633b908e172000046

def recover(st): 
    digits = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE',

    }
    
    j = 3
    digits_set = [sorted(set(digit)) for digit in digits.values()]
    digits_sorted = [sorted(digit) for digit in digits.values()]
    output = ''
    while len(st) >= 3:
        sub_str_set = sorted(set(st[0:j]))
        sub_str_sorted = sorted(st[0:j])
        if sub_str_set in digits_set and sub_str_sorted in digits_sorted:
            index = str(digits_set.index(sub_str_set))
            output += index
            st = st[1:]
            j = 3
        else: 
            j += 1
        
        if j > 6:
            st = st[1:]
            j = 2
    return output if output else 'No digits found'
        
