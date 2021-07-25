#Range Extraction kata
#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def arrange(x):
    if len(x) >= 3:
        return str(x[0])+'-'+str(x[-1])
        
    else:
        return ','.join([str(num) for num in x])
    
    return str(x[0])+'-'+str(x[-1])
    
def solution(args):
    output = []
    lst = []
    args += [-1234]
    for i, num in enumerate(args[1:]):
        print(i)
        lst.append(args[i])
        if args[i+1] - args[i] != 1:
            output.append(lst)
            lst = []
    output.append(lst)
    output = list(map(arrange, output))
    return ','.join(output).strip(',')
        
    