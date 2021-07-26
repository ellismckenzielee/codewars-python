#Rearrange number to get its maximum kata
#https://www.codewars.com/kata/563700da1ac8be8f1e0000dc

def max_redigit(num): 
    num = str(num)
    if int(num) > 0 and len(num) == 3:
        return int(''.join(sorted(num, reverse=True)))