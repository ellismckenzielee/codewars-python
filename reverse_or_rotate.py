#reverse or rotate? kata
#https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991

def revrot(strng, sz):
    output, current = "", 0
    if sz != 0 and strng != "":
        while current <= len(strng):
            indx = [current, current+sz]
            next = current + sz
            if next > len(strng):
                break
            sub = strng[indx[0]:indx[1]]
            digits = list(map(int, sub))
            total = sum(list(map(lambda x: x**3, digits)))
            if total % 2 == 0:
                output += (sub[::-1])
            else:
                output += (sub[1:] + sub[0])
            current = next
            
    return output
        