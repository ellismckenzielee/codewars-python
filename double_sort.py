#double sort kata
#https://www.codewars.com/kata/57cc79ec484cf991c900018d

def db_sort(arr):
    ints = []
    strs = []
    for char in arr:
        if type(char) == int:
            ints.append(char)
        else:
            strs.append(char)
    return sorted(ints) + sorted(strs)
            