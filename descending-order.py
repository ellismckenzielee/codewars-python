def Descending_Order(num):
    '''Function takes non-negative integer and returns digits in descending order'''
    num_list = list(map(int,str(num)))
    num_list = sorted(num_list,reverse=True)
    output =  ''.join(map(str, num_list))
    return int(output)  