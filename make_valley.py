def make_valley(arr):
    '''Make a *valley* from the array, by sorting the lists into an ascending and descending pattern'''
    arr = sorted(arr, key=int, reverse=True) 
    wings = []
    pop_l = 0
    pop_r = 0
    for i in range(0, len(arr)):
        if i % 2 == 0 or i == 0:
            print(arr[i])
            wings.insert(pop_l, arr[i])
            pop_l = pop_l +1
        else:
            if pop_r ==0:       
                wings.insert(1, arr[i])
                pop_r = pop_r -1
            else:
                wings.insert(pop_r, arr[i])
                pop_r = pop_r -1
                
    return wings