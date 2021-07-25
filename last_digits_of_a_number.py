#last digits of a number kata
#https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0

def solution(n,d):
    n = list(str(n))
    if d > len(n):
        return list(map(int, n))
    elif d <= 0:
        return []
    else:
        return list(map(int, n[-d:]))