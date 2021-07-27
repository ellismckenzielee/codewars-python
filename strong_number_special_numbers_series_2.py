#Strong Number (Special Number Series #2) kata
#https://www.codewars.com/kata/5a4d303f880385399b000001

def strong_num(number):
    total = 0
    for num in list(map(int, str(number))):
        total2 = 1
        for x in range(1, num+1):
            total2 *= x
        total += total2
    return 'STRONG!!!!' if total == number else 'Not Strong !!'

        