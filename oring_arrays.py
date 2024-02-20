## ORing Arrays kata
## https://www.codewars.com/kata/5ac5e9aa3853da25d9000102

def or_arrays(arr1, arr2, default=0):
    binary_or = []
    for i in range(max(len(arr1), len(arr2))):
        if i < len(arr1):
            elem_1 = arr1[i]
        else:
            elem_1 = default
          
        if i < len(arr2):
            elem_2 = arr2[i]
        else:
            elem_2 = default
        binary_or.append(elem_1 | elem_2)
    return binary_or
