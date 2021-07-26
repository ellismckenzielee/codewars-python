#consecutive differences kata
#https://www.codewars.com/kata/5ff22b6e833a9300180bb953

def differences(lst):
    output = [0]
    while len(lst) >= 1:
        if len(lst) != 1:
            lst = list(map(lambda x: abs(x[0] - x[1]), list(zip(lst[1:], lst[0:-1]))))
        else:
            output = lst
            break
    return output[0]