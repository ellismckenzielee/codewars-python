#sort out the men from boys kata
#https://www.codewars.com/kata/5af15a37de4c7f223e00012d

import numpy as np
def men_from_boys(arr):
    arr = np.array(arr)
    men = set(arr[arr % 2 == 0])
    boys = set(arr[arr % 2 ==1])
    return sorted(list(men)) + sorted(list(boys), reverse=True)