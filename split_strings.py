#split strings kata
#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    return [s[i:i+2] if len(s[i:i+2]) == 2 else s[i] + '_' for i in range(0, len(s), 2)]