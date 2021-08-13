#multiples of 3 or 5 kata
#https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    threes = list(range(3,number, 3))
    fives = list(range(5, number, 5))
    unique = set(threes + fives)
    return sum(unique)
  