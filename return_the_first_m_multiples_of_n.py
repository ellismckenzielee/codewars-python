#Return the first M multiples of N kata
#https://www.codewars.com/kata/593c9175933500f33400003e

def multiples(m, n):
    output = []
    for i in range(0, m):
        output.append((i+1)*n)
    return output
            