#simple letter removal kata
#https://www.codewars.com/kata/5b728f801db5cec7320000c7

def solve(st,k): 
    num, removed = 0, 0
    while removed < k and st:
        if chr(num+97) in st:
            indx = st.index(chr(num+97))
            st = st[0:indx] + st[indx+1:]
            removed += 1
        else:
            num += 1
    return st
    
        