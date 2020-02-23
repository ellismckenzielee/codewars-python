###Rule of Divisibility by 13 - codewars kata
###https://www.codewars.com/kata/564057bc348c7200bd0000ff

def thirt(n):
    '''See codewars challenge''' 
    multipliers = [1, 10, 9, 12, 3, 4]
    old_num = 0
    new_num = -1000
    while old_num != new_num:
        old_num = new_num
        new_num = 0
        for i, num in enumerate(list(str(n))[::-1]):
            new_num += (int(num) * (multipliers[i%6]))
            n = new_num
    return new_num