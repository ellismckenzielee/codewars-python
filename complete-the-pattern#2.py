###Complete the patter #2 - codewars kata
###https://www.codewars.com/users/ellismckenzielee/completed_solutions

def pattern(n):
    '''Produces pattern based on n, as specified in the kata'''
    if n <= 0:
        return ''
    str_n = str(n)
    liste_int = list(range(0,n+1))[::-1]
    liste_str = list(map(str, liste_int))
    output = ''
    for i in liste_int[:-2]:
        output += ''.join(liste_str[:i]) + '\n'
    return output + str_n