##REDUCING A PYRAMID KATA
##Given the first row of a number pyramid, the code below finds the 
##value stored in the last row 

def reduce_pyramid(base):
    pascals = pascal(len(base)-1)
    totals = [x*y for x,y in zip(pascals, base)]
    return sum(totals) 
    
def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) // (k+1))
    return line