###Convert integer to whitespce format - codewars kata 
###https://www.codewars.com/kata/55b350026cc02ac1a7000032

def whitespace_number(n):
    '''Converts number n into whitespace format'''
    binary_format = str(bin(n).split('b')[1])
    print(binary_format)
    output = ''
    if n> 0:
        output += ' '
    elif n < 0:
        output += '\t'
        
    output +=  binary_format.replace('1', '\t').replace('0', ' ')
    return output + '\n'