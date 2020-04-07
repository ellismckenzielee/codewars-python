###Backspaces in String - codewars kata
###https://www.codewars.com/kata/5727bb0fe81185ae62000ae3


def clean_string(s):
    '''Returns a string based on s, which has a backspace 
    wherever a hash symbol is found'''
    output = ''
    for i, letter in enumerate(s):
        if letter == '#':
            output = output[:-1]
        else:
            output += letter
    return output