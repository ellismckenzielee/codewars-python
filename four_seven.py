#Four/Seven kata
#https://www.codewars.com/kata/5ff50f64c0afc50008861bf0

def solution(n):
    vals = [4,7]
    try:
        return vals[vals.index(n)-1]
    except:
        return False