#thinking & testing: something capitalized kata
#https://www.codewars.com/kata/56d93f249c844788bc000002

def testit(s):
    if s == '':
        return ''
    s = s.split(' ')
    output_string = ''
    for string in s:
        letters = list(string)
        letters[-1] = letters[-1].title()
        string = ''.join(letters)
        output_string += string + ' '
    return ''.join(list(output_string)[:-1])