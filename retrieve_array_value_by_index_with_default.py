#Retrieve array value by index with default kata
#https://www.codewars.com/kata/515ceaebcc1dde8870000001

def solution(items, index, default_value):
    try:
        return items[index]
    except:
        return default_value    