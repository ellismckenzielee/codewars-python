#Moving zeros to the end kata
#https://www.codewars.com/kata/52597aa56021e91c93000cb0


#REFACTORED SOLUTION
def move_zeros(array):
    zeros = []
    output = []
    for elem in array:
        if elem == 0 and not isinstance(elem, bool):
            zeros.append(0)
        else:
            output.append(elem)
            
    return output + zeros


#PREVIOUS SOLUTION
def conversion(x):
    if type(x) in [float, int]:
        return str(x)
    elif type(x) == str:
        if '-' not in x and x.isnumeric():
            return float(x)  
        elif '-' in x:
            return -float(x[1:])
    return x
    
def str_zeros(x):
    if x == '0':
        return '!'
    elif x == '0.0':
        return '!!'
    elif x == '!':
        return '0'
    elif x == '!!':
        return '0.0'
    return x
        
def move_zeros(array):
    array = list(map(str_zeros, array))
    array = list(map(conversion, array))
    zeros = array.count('0') + array.count('0.0')
    array = list(filter(lambda a: a not in ['0', '0.0'], array))
    array = list(map(conversion, array))
    output = []
    for char in array + [0 for zero in range(zeros)]:
        if type(char) == float:
            if int(char) == char:
                output.append(int(char))
        else:
            output.append(char)
    output = list(map(str_zeros, output))
    return output