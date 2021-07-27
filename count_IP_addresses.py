#Count IP Addresses kata
#https://www.codewars.com/kata/526989a41034285187000de4

def ips_between(start, end):
    start = list(map(int, start.split('.')))
    end = list(map(int, end.split('.')))
    difference = list(map(lambda x: x[1] - x[0], zip(start,end)))
    totals = list(map(lambda x: x[1] * x[0], zip(difference,[256**3, 256**2,256, 1])))
    return sum(totals)    