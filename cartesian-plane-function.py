#Functions below return the output of functions f (sumin), g (sumax) and h (sumsum)
#See kata 'Functions of Integers on Cartesian Plane' for more information
def sumin(n):
    total = 0
    for i in range (1,n):
        total += ((i*(n+1-i)) + (i*(n-i)))
    return total + n
    
def sumax(n):
    total = 0
    for i in range (1, n):
        total += ((n+1-i)*(n+1-i)) + ((n+1-i)*(n-i))
    return total + 1 
    
def sumsum(n):
    return sumin(n) + sumax(n)