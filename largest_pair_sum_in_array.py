## Largest pair sum in array kata
## https://www.codewars.com/kata/556196a6091a7e7f58000018

def largest_pair_sum(numbers): 
    return sum(sorted(numbers, reverse=True)[0:2])