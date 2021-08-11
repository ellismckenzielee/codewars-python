#simple fun #125: array equalization kata
#https://www.codewars.com/kata/58a3c836623e8c72eb000188

def array_equalization(a, k):
    nums = sorted(set(a))
    output = 100
    for num in nums:
        a_copy = a.copy()
        total = 0
        while len(a_copy) >=k:
            if a_copy[0] != num:
                del a_copy[0:k]
                total += 1
            else:
                del a_copy[0]
        if all(list(map(lambda x: x ==num, a_copy))) == False:
            total += 1
        if total < output:
            output = total
    return output
