#decipher this! kata
#https://www.codewars.com/kata/581e014b55f2c52bb00000f8

import re
def decipher_this(string):
    words, output = string.split(' '), []
    for word in words:
        num = re.findall('[0-9]+', word)
        remainder = re.findall('[a-zA-Z]+', word)
        if remainder:
            remainder = list(remainder[0])
            if len(remainder) > 1: 
                remainder[0], remainder[-1] = remainder[-1], remainder[0]
        else:
            remainder = ''
        output.append(chr((int(num[0])))+''.join(remainder))
    return ' '.join(output)
        