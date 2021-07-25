#Greatest Common Factor of an Array kata
#https://www.codewars.com/kata/5849169a6512c5964000016e

def greatest_common_factor(seq): 
    seq = sorted(seq)
    for num in list((range(1, seq[0]+1)))[::-1]:
        divisible = list(map(lambda x: x%num == 0, seq))
        if all(divisible):
            return num