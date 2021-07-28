#duplicate sandwich kata
#https://www.codewars.com/kata/5f8a15c06dbd530016be0c19

def duplicate_sandwich(arr):
    appeared = []
    for i, item in enumerate(arr):
        if item not in appeared:
            appeared.append(item)
        else:
            return arr[arr.index(item)+1:i]