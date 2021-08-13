#extra perfect numbers (special numbers series #7)
#https://www.codewars.com/kata/5a662a02e626c54e87000123

def extra_perfect(n):
    return list(range(1, n+1, 2)) if n % 2 == 1 else list(range(1,n,2)) 