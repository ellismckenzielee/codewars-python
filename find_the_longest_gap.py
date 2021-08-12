#find the longest gap kata
#https://www.codewars.com/kata/55b86beb1417eab500000051

def gap(num):
    binary = str(bin(num)).strip('0').split('b')[1]
    binary = binary.split('1')
    return max(list(map(lambda x: len(x), binary)))