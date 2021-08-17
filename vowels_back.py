#vowels back kata
#https://www.codewars.com/kata/57cfd92c05c1864df2001563

def vowel_back(st):
    new_string = ''
    for letter in list(st):
        if letter == 'c' or letter == 'o':
            x = -1
        elif letter == 'd':
            x = -3
        elif letter == 'e':
            x = -4
        else:
            if letter in 'aiou':
                x = -5
            else:
                x = 9
        num = ord(letter)
        new_num = num + x
        if new_num > 122:
            new_num = 96 + (new_num - 122)
        elif new_num < 97:
            new_num = 122 + (new_num - 96)
        
        new_letter = chr(new_num)
        if new_letter in list('code'):
            new_letter = letter 
        
        new_string += new_letter
    return new_string
         
    