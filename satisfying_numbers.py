#Satisfying numbers kata
#https://www.codewars.com/kata/55e7d9d63bdc3caa2500007d

def smallest(n):
    total = 1
    for num in range(1, n+1):
        for i in range(1, num + 1):
            if num%i == 0 and i not in (1, num):
                break
            elif num == i or num == 1:
                pwr = 1
                while True and num != 1:
                    tot = num ** pwr
                    if tot <= n:
                        pwr += 1
                    else:
                        total *= num**(pwr-1)
                        break
    return total
                        