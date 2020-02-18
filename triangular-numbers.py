###SUM of Triangular Numbers Kata
def sum_triangular_numbers(n):
    '''Uses formula to find triangular numbers and adds these to total'''
    total = 0
    for i in range(n+1):
        total += sum(list(range(1,i+1)))
    return total 