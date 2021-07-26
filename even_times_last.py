#Even times last kata
#https://www.codewars.com/kata/5a1a9e5032b8b98477000004

def even_last(numbers): 
    total = 0
    if numbers:
        last = numbers[-1]
        numbers = [num for i, num in enumerate(numbers) if i % 2 ==0]
        total = sum(numbers) * last
    return total