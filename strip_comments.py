#strip comments kata
#https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string,markers):
    output = ''
    marked = False
    for i, char in enumerate(string):
        if marked == False:
            if char in markers:
                marked = True
            else:
                output += char
        elif marked == True:
            if char == '\n':
                marked = False
                if string[-1] != '\n':
                    output = output.rstrip(' ')
                output += '\n'
    if output[-1:] != '\n':
        return output.rstrip()
    else:
        return output
