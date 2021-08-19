#sums of parts kata
#https://www.codewars.com/kata/5ce399e0047a45001c853c2b

import numpy as np
def parts_sums(ls):
    reduction = np.cumsum(ls)
    if reduction.size == 0:
        return [0]
    reduction = np.insert(reduction, 0, 0, axis=0)
    total = np.ones(len(ls)+1)*reduction[-1]
    final = (total - reduction)
    return final.tolist()