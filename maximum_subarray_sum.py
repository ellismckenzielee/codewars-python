#maximum subarray sum kata
#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    mx = 0 
    substr =[]
    for i in range(0, len(arr)):
        for j in range(0, len(arr) + 1 - i):
            total =  sum(arr[j:j+i+1])
            if total > mx:
                mx = total
    return mx
