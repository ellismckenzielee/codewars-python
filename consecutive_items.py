#consecutive items kata
#https://www.codewars.com/kata/5f6d533e1475f30001e47514

def consecutive(arr, a, b):
    return True if sorted([a, b]) in [sorted([arr[i], arr[i+1]]) for i in range(len(arr)-1)] else False
    