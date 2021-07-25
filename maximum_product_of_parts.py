#Maximum product of parts kata
#https://www.codewars.com/kata/5a3a95c2e1ce0efe2c0001b0

def maximum_product_of_parts(n):
    n = list(map(int, str(n)))
    totals = []
    for i in range(1, len(n)):
        for j in range(i+1, len(n)):
            parts = [n[:i], n[i:j], n[j:]]
            new_parts = []
            total = 1
            for part in parts:
                part = list(map(str, part))
                part = ''.join(part)
                part = int(part)
                total *= part
            totals.append(total)
    return max(totals)            
            