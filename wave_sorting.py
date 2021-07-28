#wave sorting kata
#https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1

def wave_sort(a):
    a.sort()
    for i in range(0, len(a)-1, 2):
        a[i], a[i+1] = a[i+1], a[i]