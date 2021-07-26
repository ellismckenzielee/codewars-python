#Limit string length - 1 kata
#https://www.codewars.com/kata/5208fc3cb613bc725f000142

def solution(st, limit): 
    print(len(st), limit)
    return st[0:limit] + '...' if limit < len(st) else st