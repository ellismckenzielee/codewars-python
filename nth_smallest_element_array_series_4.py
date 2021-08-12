#nth smallest element (array series #4) kata
#https://www.codewars.com/kata/5a512f6a80eba857280000fc

def nth_smallest(arr, pos):
    return sorted(arr)[pos-1]