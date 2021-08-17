#is integer array? kata
#https://www.codewars.com/kata/52a112d9488f506ae7000b95

def is_int_array(arr):
    print(arr)
    if not isinstance(arr, list):
        return False
    
    elif arr == []:
        return True
   
    return all(map(element_check, arr))
  
def element_check(x):
    print(x)
    if x == None:
        return False
    elif type(x) == str:
        return False
    else:
        x = float(x)
        if x.is_integer():
            return True
        else:
            return False