#N smallest elements in original order
#https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

def first_n_smallest(arr, n):
    ordered = sorted(arr)
    smallest = ordered[:n]
    print(smallest)
    output = []
    for num in arr:
        if num in smallest and len(output) <n:
            output.append(num)
            smallest.remove(num)
    return output