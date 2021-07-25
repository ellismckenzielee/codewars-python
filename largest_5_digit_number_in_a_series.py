#Largest 5 digit number in a series kata
#https://www.codewars.com/kata/51675d17e0c1bed195000001

def solution(digits):
    max_num = 0
    for i in range(len(digits)-4):
        number = int(digits[i:i+5])
        if number > max_num:
            max_num = number
    return max_num