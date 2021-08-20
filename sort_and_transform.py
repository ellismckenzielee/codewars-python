#sort and transform kata
#https://www.codewars.com/kata/57cc847e58a06b1492000264

def sort_transform(arr):
    output_string = ''
    for command in ['a','b','c','d']:
        output_string += string_appender(output_string, arr, command)

    return output_string[:-1]
    
def string_appender(strg, arr, command):
    if command in ('b', 'd'):
        arr = sorted(arr)
    elif command == 'c':
        arr = sorted(arr)[::-1]
    return str(chr(arr[0])) + str(chr(arr[1])) + str(chr(arr[-2])) + str(chr(arr[-1])) + '-'
     