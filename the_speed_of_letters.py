#the speed of letters kata
#https://www.codewars.com/kata/5fc7caa854783c002196f2cb

def speedify(st): 
    if st:
        st = list(st)
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        spaces = max([i + alphabet.index(letter) for i, letter in enumerate(st)]) + 1
        output = [' ' for space in range(spaces)]
        for i, letter in enumerate(st):
            output[i + alphabet.index(letter)] = letter
        return ''.join(output)
    return st
    
        