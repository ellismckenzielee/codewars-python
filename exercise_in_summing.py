#exercise in summing kata
#https://www.codewars.com/kata/52cd0d600707d0abcd0003eb

def minimum_sum(values, n):
  '''sum the n smallest integers in the array values (not necessarily ordered)'''

  return sum(sorted(values)[:n])

def maximum_sum(values, n):
  '''sum the n largest integers in the array values (not necessarily ordered)'''
  return sum(sorted(values, reverse=True)[:n])