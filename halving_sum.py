#halving sum kata
#https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d

def halving_sum(n): 
    num = n
    total = n
    while num > 0.1:
        num  //= 2
        total += num
    return total            