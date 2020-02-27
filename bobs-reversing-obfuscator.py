###Bob's reversing obfuscator - kata
###https://www.codewars.com/kata/559ee79ab98119dd0100001d

def decoder(encoded, marker):
    '''Returns decoded string'''
    encoded = encoded.replace(marker, '#')
    marker = '#'
    encoded = encoded[::-1]
    output= ''
    for letter in encoded:
        if letter != marker:
            output += letter
        if letter == marker:
            output = output[::-1]
    return output[::-1]