#simple fun #23: square digits sequence kata
#https://www.codewars.com/kata/5886d65e427c27afeb0000c1/solutions/python

def square_digits_sequence(n):
    nums = []
    while n not in nums:
        nums.append(n)
        n = sum(list(map(lambda x: int(x)**2, list(str(n)))))
    return len(nums) + 1