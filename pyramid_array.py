#pyramid array kata
#https://www.codewars.com/kata/515f51d438015969f7000013

def pyramid(n):
    return [[1 for i in range(n+(j-n))] for j in range(1, n+1)]