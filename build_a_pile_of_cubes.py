#build a pile of cubes kata
#https://www.codewars.com/kata/5592e3bd57b64d00f3000047

def find_nb(m):
    total = 0 
    cubes = 1
    while total < m:
        total += cubes ** 3
        cubes += 1
        if total == m:
            return cubes - 1
    return -1
        

            
        
        