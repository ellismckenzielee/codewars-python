#fix array sequence kata
#https://www.codewars.com/kata/5b7bae02402fb702ce000159

def find_next(num, rem):
    if num % 3 == 0:
        next_num = int(num/3)
        if next_num in rem:
            return next_num
    next_num = int(num*2)
    if next_num in rem:
        return next_num
    return False
        
    
def solve(arr):
    for num in arr:
        remaining = arr.copy()
        current, index = num, 0
        output = []
        while index != -1:
            index = remaining.index(current) if current in remaining else -1
            current = remaining.pop(index)
            output.append(current)
            if len(output) == len(arr):
                return output
            current = find_next(current, remaining)
            if current == False:
                print(False)
                break

    
        
    