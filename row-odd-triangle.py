###Row of the odd triangle - codewars kata
###Find and return row 'n' of an odd triangle, which starts with one
def odd_row(n):
    multipliers = list(map(lambda x: x*2, list(range(n))))
    start = sum(multipliers) + 1
    return list(range(start, start + (2*n), 2))