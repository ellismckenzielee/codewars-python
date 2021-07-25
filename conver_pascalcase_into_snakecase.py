#Convert PascalCase into snake_case kata
#https://www.codewars.com/kata/529b418d533b76924600085d

def char_replacer(chr):
    if chr.isupper():
        return '_' + chr.lower()
    return chr

def to_underscore(string):
    return ''.join(list(map(char_replacer, str(string)))).strip('_')
    