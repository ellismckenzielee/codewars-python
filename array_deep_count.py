# Array Deep Count
# https://www.codewars.com/kata/596f72bbe7cd7296d1000029/

def deep_count(a):
    count = 0 
    for item in a:
        if type(item) == list:
            count += deep_count(item)
        count += 1
    return count
    
