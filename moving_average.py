#moving average kata
#https://www.codewars.com/kata/5c745b30f6216a301dc4dda5

def moving_average(values,n):
    print(n)
    print(values)
    return [sum(values[i:i+n])/n for i in range(len(values)-n+1)] if n != 0 and n <= len(values) else None