#sort the vowels kata
#https://www.codewars.com/kata/59e49b2afc3c494d5d00002a

def sort_vowels(s):
    if type(s) == int or s == None:
        return ''
    
    output = ''
    for letter in s:
        if letter.lower() in 'aeiou':
            letter = '|' + letter
        else:
            letter += '|'
        output += letter +'\n'
    return output.strip('\n')