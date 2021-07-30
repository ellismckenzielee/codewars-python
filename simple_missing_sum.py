#simple missing sum kata
#https://www.codewars.com/kata/5a941f3a4a6b34edf900006f

def solve(arr):
    arr = sorted(arr)
    num = 1
    for i in arr:
        if i <= num:
            num += i
        else:
            break
    return num
        
    
                