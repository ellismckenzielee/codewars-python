#reverse every other word in the string
#https://www.codewars.com/kata/58d76854024c72c3e20000de

def reverse_alternate(string):
    words = string.split(' ')
    words = list(filter(lambda a: a != '', words))
    output = ''
    for i, word in enumerate(words):
        if i % 2 == 1:
           output += word[::-1] + ' '
        else:
            output += word + ' '
    return output.strip()
    