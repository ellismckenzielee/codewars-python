#Put a letter in a column kata
#https://www.codewars.com/kata/563d54a7329a7af8f4000059

def build_row_text(index, character):
    output = list('| | | | | | | | | |')
    output[index*2+1] = character
    return ''.join(output)
    