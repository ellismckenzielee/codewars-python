###Password Validator - codewars kata
###https://www.codewars.com/kata/56a921fa8c5167d8e7000053

def password(string):
    '''Checks if password meets criteria (see link) and returns
    True or False depending on whether all conditions are satisfied'''
    upper = False
    lower = False
    number = False
    if string == '':
        return False
    for i, char in enumerate(string):
        print(char)
        if char.isupper():
            print('UPPER')
            upper = True
        elif char.islower():
            print('LOWER')
            lower = True
        elif char.isnumeric():
            print('NUMERIC')
            number = True
    if i >= 7 and (upper == True) and (lower == True) and (number == True):
        return True
    return False