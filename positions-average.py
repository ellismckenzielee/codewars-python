import numpy as np
def pos_average(s):
    '''Find common positions in strings, and return as a percentage of total positions'''
    s = s.replace(',','')
    s = s.split(' ')
    total = (len(s)*(len(s)-1))/2
    sequence_array = []
    for sequence in s:
        sequence_array.append(list(sequence))
    
    arr = np.array(sequence_array)
    counter = 0
    
    for i in range(0, arr.shape[1]):
        print(arr[:,i])
        unique, counts = np.unique(arr[:,i], return_counts=True)
        print('unique', unique)
        for k in range(0, len(counts)):
            print(counts[k])
            if counts[k] > 1:
                counter += np.sum(np.arange(1, counts[k]))
                
    return counter/(total*len(s[0]))*100