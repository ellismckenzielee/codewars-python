#simple fun #132: number of carries kata
#https://www.codewars.com/kata/58a6568827f9546931000027

def number_of_carries(a, b):
    carries = 0 
    a = [0 for i in range(0, len(str(b))-len(str(a)))] + list(map(int,list(str(a))))
    b = [0 for i in range(0, len(a)-len(str(b)))] + list(map(int,list(str(b))))
    a, b = a[::-1], b[::-1]
    remainder = 0 
    for i in range(len(a)):
        if remainder == 0:
            total = a[i] + b[i]
        else:
            total = a[i] + b[i] + remainder
        
        if total >= 10:
            remainder = total // 10
            carries += 1
        else:
            remainder = 0 
    return carries
     
