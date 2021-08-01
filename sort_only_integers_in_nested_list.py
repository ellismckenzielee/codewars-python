#sort only integers in nested list kata
#https://www.codewars.com/kata/5a4bdd73d8e145f17d000035

def sort_nested_list(A):
    vals = []
    for sub_lst in A:
        for lst in sub_lst:
            vals += lst
    vals = sorted(vals)
    for i, sub_lst in enumerate(A):
        for j, lst in enumerate(sub_lst):
            for k in range(len(lst)):
                A[i][j][k] = vals.pop(0)
    return A