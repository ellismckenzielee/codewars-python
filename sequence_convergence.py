#sequence convergence kata
#https://www.codewars.com/kata/59971e64bfccc70748000068

def move(n):
    if n < 10:
        return n*2
    else:
        total = 1
        for x in str(n):
            print(x)
            if x != '0':
                total *= int(x)
        return total + n
    
def convergence(n):
    base_seq = 1
    other_seq = n
    converged = False
    i = 0
    while converged == False:
        if base_seq < other_seq:
            base_seq = move(base_seq)
        elif base_seq != other_seq:
            other_seq = move(other_seq)
            i += 1
        else:
            return i

        
            