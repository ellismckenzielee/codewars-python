#sum - square even, root odd kata
#https://www.codewars.com/kata/5a4b16435f08299c7000274f

def sum_square_even_root_odd(nums):
    output = []
    for num in nums:
        if num % 2 == 0:
            total = num**2
        else:
            total = num**0.5
        output.append(total)
    return round(sum(output),2)