#Simple Fun #243: Perfect Team Of Minimal Size kata
#https://www.codewars.com/kata/590a924c7dfc1a238d000047

from itertools import permutations
def perfect_team_of_minimal_size(n, candidates):
    for i in range(1, n+1):
        all = list(permutations(candidates, i))
        for perm in all:
            items = []
            for candidate in perm:
                for cat in candidate:
                    items.append(cat)
            if len(set(items)) == n:
                return i + 1
    return -1
        
                    
                    
            
                    
                