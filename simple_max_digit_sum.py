#simple max digit sum kata
#https://www.codewars.com/kata/5b162ed4c8c47ea2f5000023

def digit_sum(num):
    tot = 0
    while num > 0:
        tot += (num % 10)
        num = int(num /10)
    return tot 

def solve(n):
    total = digit_sum(n)
    largest = n
    print(n)
    i = 1
    while n > 0:
        n = n - (n % (10)**i) -1
        new_total = digit_sum(n)
        i += 1
        if new_total > total:
            total = new_total
            largest = n
    return largest