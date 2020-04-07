###Fill the HDD - codewars kata
###https://www.codewars.com/kata/5d49c93d089c6e000ff8428c

def save(sizes, hd): 
    '''Returns number of files that can be copied to HDD
    based on file and HDD sizes'''
    total = 0
    for i in range(len(sizes)):
        total += sizes[i]
        if total > hd:
            return i 
    return len(sizes)