#draw stairs kata
#https://www.codewars.com/kata/5b4e779c578c6a898e0005c5

def draw_stairs(n):
    output_string = ''
    for num in range(0,n-1):
        output_string += ' '*num + 'I\n'
    output_string +=  ' '*(n-1) + 'I'
    return output_string