#+1 Array kata
#https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

def up_array(arr):
    cond = list(filter(lambda x: x < 0 or x//10 >= 1, arr)) != []  
    if cond == False and arr != []:
        arr = list(map(str, arr)) 
        num = int(''.join(arr)) + 1
        return list(map(int,str(num)))