## The alphabet product
## https://www.codewars.com/kata/63b06ea0c9e1ce000f1e2407/train/python

def alphabet(ns):
    products = []
    nums = []
    for index, current in enumerate(sorted(ns)):
        print(index, current)
        if current in products:
            index = products.index(current)
            products.pop(index)
        else:
            for num in nums:
                products.append(num * current)
            nums.append(current)
            
    return nums[-1]
