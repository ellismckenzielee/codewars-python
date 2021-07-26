#Get the middle character kata
#https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    i, j = 1, 0
    if len(s) % 2 == 0:
        i = 2
        j = -1
    return s[int(len(s)/2+j):int(len(s)/2)+i+j]