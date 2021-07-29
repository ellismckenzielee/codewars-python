#longest common subsequence kata
#https://www.codewars.com/kata/52756e5ad454534f220001ef

def lcs(x, y):
    x = list(filter(lambda x1: x1 in y,x))
    y = list(filter(lambda x1: x1 in x,y))
    if [] in (x,y):
        return ''
    elif x == y:
        return ''.join(x)
    else:
        both = [x, y]
        lens = [len(x), len(y)]
        mindex = lens.index(min(lens[0],lens[1]))
        maxdex = lens.index(max(lens[0],lens[1]))
        output = ''
        for i, letter in enumerate(both[mindex]):
            try :
                index = both[maxdex].index(letter)
                both[maxdex] = both[maxdex][index:]
                output += letter
            except:
                continue
        return output
                