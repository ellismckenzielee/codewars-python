#Integers: Recreation One kata
#https://www.codewars.com/kata/55aa075506463dac6600010d

import math
def find_divisors(num):
    divisors = set()
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            divisors.add(i)
            divisors.add(int(num / i))
    total = sum(list(map(lambda x: x**2, list(divisors))))
    if (int(math.sqrt(total)) **2 == total ) and total > 0:
        return [num, total]
    return False

def list_squared(m, n):
    output = []
    for num in range(m,n+1):
        soltn = find_divisors(num)
        if soltn:
            output.append(soltn)
    return output    