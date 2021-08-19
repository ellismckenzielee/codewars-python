#sum of odd numbers kata
#https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

def row_sum_odd_numbers(n):
    powers = list(range(2, n))
    start_point = 1
    if n ==1:
        return 1
    for power in powers:
        start_point += 2*power
    total = list(range(start_point + 2, start_point + ((n+1)*2), 2))
    return sum(total)   