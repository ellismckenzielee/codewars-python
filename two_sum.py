#Two Sum kata
#https://www.codewars.com/kata/52c31f8e6605bcc646000082

def two_sum(numbers, target):
    for i, num in enumerate(numbers):
        other_num = target - num
        if other_num in numbers and numbers.index(other_num) != i:
            return [i, numbers.index(target-num)]
    