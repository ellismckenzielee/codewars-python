# Credit Card Mask kata
# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

# return masked string
def maskify(cc):
    return '#' * (len(cc) - 4) + cc[-4:]
