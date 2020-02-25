###Make the Deadfish Swim - codewars kata
###https://www.codewars.com/kata/51e0007c1f9378fa810002a9/python

def parse(data):
    '''Returns a list according to the data input'''
    output = 0
    output_array = []
    for letter in data:
        if letter == 'i':
            output += 1
        elif letter == 'd':
            output -= 1
        elif letter == 's':
            output *= output
        elif letter == 'o':
            output_array.append(output) 
    return output_array
            