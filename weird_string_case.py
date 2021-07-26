#WeIrD StRiNg CaSe kata
#https://www.codewars.com/kata/52b757663a95b11b3d00062d

def to_weird_case(string):
    output = ''
    for word in string.split(' '):
        output += ' ' + ''.join([char.title() if i%2 == 0 else char for i, char in enumerate(word) ])
    return output.strip(' ')