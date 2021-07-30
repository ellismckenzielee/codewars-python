#simple frequency sort kata
#https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc

def solve(arr):
    nums = set(arr)
    frequencies = {}
    for num in nums:
        if arr.count(num) in frequencies:
            frequencies[arr.count(num)].append(num)
        else:
            frequencies[arr.count(num)] = [num]
    output = []
    for count in sorted(frequencies.keys(), reverse=True):
        for num in sorted(frequencies[count]):
            output.extend([num for y in range(count)])
    return output