## counting duplicates across multiple lists
## https://www.codewars.com/kata/6113c2dc3069b1001b8fdd05/

def count_duplicates(name,age,height):
    prev = []
    duplicates = 0
    for i, n in enumerate(name):
        profile = [n, age[i], height[i]]
        if profile in prev:
            duplicates += 1
        else:
            prev.append(profile)
    return duplicates