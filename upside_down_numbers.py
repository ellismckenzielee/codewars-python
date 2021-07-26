#upside down numbers kata
#https://www.codewars.com/kata/59f7597716049833200001eb

def solve(a, b):
    pair1 = ['0','1','6','8','9']
    pair2 = ['0','1','9','8','6']
    numbers = []
    for num in range(a, b):
        num = str(num)  
        if len(num) == 1:
            num += num
        mid_point = int(len(num)/2)
        for i in range(0, mid_point):
            num1 = num[i]
            num2 = num[-(i+1)]
            if num1 not in pair1 or num2 not in pair1:
                break
            else:
                if pair1.index(num1) != pair2.index(num2):
                    break
            if i == mid_point - 1:
                if len(num) % 2 == 1:
                    if num[mid_point] not in ('0','1','8'):
                        break
                numbers.append(num)
    print(numbers, a, b)
    return len(numbers)