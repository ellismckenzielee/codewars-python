#Validate Credit Card Number kata
#https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2

def validate(n):
    n = list(map(int, str(n)))
    start_num = [0,1][len(n) % 2]
    n = [x*2 if (i+start_num)%2 == 0 else x for i, x in enumerate(n)]   
    n = [x-9 if x > 9 else x for i, x in enumerate(n)]  
    return sum(n) % 10 == 0
    