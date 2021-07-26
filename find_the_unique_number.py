#find the unique number kata
#https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    unique = set(arr)
    for num in unique:
        new_arr = arr.copy()
        index = new_arr.index(num)
        new_arr.pop(index)
        if num in new_arr:
            continue
        else:
            return num
        