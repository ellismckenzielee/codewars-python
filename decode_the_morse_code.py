#decode the morse code kata
#https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    morse_code = morse_code.lstrip().rstrip()
    morse_code = morse_code.split('   ')
    output = []
    
    for code in morse_code:
        output.append(''.join(list(map(lambda x: MORSE_CODE[x], code.split(' ')))))
    output = ' '.join(output)
    
    return output
    
