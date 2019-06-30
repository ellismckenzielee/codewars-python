##SUM OF DIGITS/DIGITAL ROOT KATA
##Function finds the recursive sum of numbers in number 'n'
##For example, if n = 16, ==> total = 1 + 6

def digital_root(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    numbers = list(map(int, list(n)))
    return digital_root(sum(numbers))