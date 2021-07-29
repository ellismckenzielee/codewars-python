#peak array index kata
#https://www.codewars.com/kata/5a61a846cadebf9738000076

def peak(arr):
    for peak in range(0,len(arr)):
        if sum(arr[:peak]) == sum(arr[peak+1:]):
            return peak
    return -1