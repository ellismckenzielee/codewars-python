# The @ Operator kata
# https://www.codewars.com/kata/631f0c3a0b9cb0de6ded0529/train/python
def evaluate(equation):
    nums = list(map(int, equation.split(' @ ')))
    total = nums[0]
    for num in nums[1:]:
        try:
            total = ((total + num) + (total - num) + (total * num) + (total // num))
        except:
            return None
    return total
