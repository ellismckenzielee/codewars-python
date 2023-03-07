# Delta Generators kata
# https://www.codewars.com/kata/6040b781e50db7000ab35125
def delta(values, n):
    values = iter(values)
    if (n == 0):
        return values
    else:
        return delta(diff(values),n-1)
            
def diff(iterable):
    one = next(iterable)
    while True:
        try:
            two = next(iterable)
            yield two.__sub__(one)
            one = two
        except StopIteration:
            return
    
