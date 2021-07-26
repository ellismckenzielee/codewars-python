#Convert lambda to def kata
#https://www.codewars.com/kata/605d25f4f24c030033da9afb

def convert_lambda_to_def(string):
    name, rhs = string.split(' = ')
    lmdba, rtn = rhs.split(': ')
    param = lmdba.split('lambda ')[-1]
    return f"def {name}({param}):\n    return {rtn}"