#sum of odd cubed numbers kata
#https://www.codewars.com/kata/580dda86c40fa6c45f00028a


def cube_odd(arr):
    total = 0 
    for num in arr:
        if (type(num) != int):
            return None
        if num % 2 != 0:
            total += num**3
    return total