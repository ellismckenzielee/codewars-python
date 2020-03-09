###Yes No Yes No - codewars kata
### https://www.codewars.com/kata/573c84bf0addf9568d001299/train/python

def yes_no(arr):
    if not arr:
        return []
    output = [arr[0]]
    arr = arr[1:]
    
    while len(arr) > 1:
        output.append(arr[1])
        del arr[1]
        arr.append(arr[0])
        del arr[0]
    if arr:
        output.append(arr[0])
    return output
    
        
                