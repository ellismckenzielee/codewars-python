#flatten() kata
#https://www.codewars.com/kata/513fa1d75e4297ba38000003

def list_sorter(lst):
    output = []
    for elem in lst:  
        if type(elem) == list:
            output += list_sorter(elem)
        else:
            output.append(elem)
    return output

def flatten(*args):
    output = []
    for arg in [*args]:
        if type(arg) == list:
            print('list', arg)
            output += list_sorter(arg)
        else:
            output.append(arg)
    return output
    