#Make a window kata
#https://www.codewars.com/kata/59c03f175fb13337df00002e

def make_a_window(num): 
    output = ''
    for i in range(5):
        if i in (0,4):
            edge, middle, type = '-', '-', '-'
            n = 1
        elif i == 2:
            edge, middle, type = '|', '+', '-'
            n = 1
        else:
            edge, middle, type = '|', '|', '.'
            n=num
        output += (n*(edge + type*num + middle + type*num + edge +'\n'))
    return output[:-1]