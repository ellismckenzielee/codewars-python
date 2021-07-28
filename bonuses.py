#bonuses kata
#https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6

def bonus(arr, s):
    minimum = min(arr)
    ratios = [(num/minimum)**-1 for num in arr]
    total = sum(ratios)
    return [round(s*ratio/total) for ratio in ratios]
    