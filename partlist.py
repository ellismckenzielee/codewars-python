def partlist(arr):
    '''Returns all the ways to divide a list'''
    output_list = []
    for i in range(0,len(arr)-1):
        output_list.append((' '.join(arr[:i+1]), ' '.join(arr[i+1:]),))
        
    return output_list