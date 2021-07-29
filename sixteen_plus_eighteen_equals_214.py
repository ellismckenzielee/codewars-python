#16+18=214 kata
#https://www.codewars.com/kata/5effa412233ac3002a9e471d

def add(num1, num2):
    str_1, str_2 = str(num1), str(num2)
    max_length = max(len(str_1), len(str_2))
    str_1 = '0'*(max_length - len(str_1)) + str_1
    str_2 = '0'*(max_length - len(str_2)) + str_2
    result = list(map(lambda x: str(int(x[0]) + int(x[1])), list(zip(str_1, str_2))))
    return int(''.join(result))