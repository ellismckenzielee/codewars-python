#Counting duplicates kata
#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

from collections import Counter

def duplicate_count(text):
    text = list(map(lambda x: x.lower(), text))
    result = Counter(text)
    total = 0
    for key, value in result.items():
        if value > 1:
            total += 1
    return total 
     