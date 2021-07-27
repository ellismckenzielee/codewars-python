#format words into a sentecne kata
#https://www.codewars.com/kata/51689e27fe9a00b126000004

def format_words(words):
    output = ''
    if words:
        words = list(filter(lambda x: x!= '', words))
        if len(words) <= 2:
            output += ' and '.join(words)
        else:
            output += ', '.join(words[:-2]) + ', ' + ' and '.join(words[-2:])
    
    return output