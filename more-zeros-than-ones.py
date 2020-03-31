###More Zeros than Ones - codewars kata
###https://www.codewars.com/kata/5d41e16d8bad42002208fe1a


def check_zeros(letter):
    original_letter = letter 
    letter = bin(ord(letter)).split('b')
    print(letter)
    letter = letter[-1]
    ones = letter.count('1')
    zeros = letter.count('0')
    return original_letter if zeros > ones else ''
    
def more_zeros(s):
    '''Returns a new s whereby elements which, in binary form, have fewer
    zeros than ones, have been removed''' 
    used_letters = set()
    output = []
    for letter in s:
        letter = check_zeros(letter)
        if letter and letter not in used_letters:
            output.append(letter)
        used_letters.add(letter)
    return output