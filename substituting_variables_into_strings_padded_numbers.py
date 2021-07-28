#substituting variables into strings: padded numbers kata
#https://www.codewars.com/kata/51c89385ee245d7ddf000001

def solution(value):
    value = str(value)
    return 'Value is ' + '0'*(5-len(value)) + value
