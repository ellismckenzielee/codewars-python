##ULTIMATE ARRAY REVERSER KATA
##Reverse an array in such a way, that their string stay the same lengths

def reverse(a):
    start_point = 0
    output = []
    a_string = ''.join(a)[::-1]
    for item in a:
        end_point = start_point + len(item)
        output.append(a_string[start_point:end_point])
        start_point = end_point
    return output