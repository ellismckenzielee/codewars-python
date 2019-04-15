def square_up(n):
    '''Return a list depending on the value of nu
    for example: n = 2 ==> [0,1,2,1]. n = 3 ==> [0, 0, 0, 0, 2, 1, 3, 2, 1] '''
    arr_to_n = list(range(1,n+1))
    arr_to_n.sort(reverse=True)
    output_list = []
    previous_list = [0]*n
    for i in range(1, n+1):
        previous_list[-i] = arr_to_n[-i]
        output_list.extend(previous_list)
    return [num if num >= 0 else 0 for num in output_list]