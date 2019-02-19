import re
def printer_error(s):
    '''Counts the number of printer errors (denoted by a letter not in a-m)'''
    matches = re.findall(r'[a-m]',s)
    return str(len(s)-len(matches))+'/'+str(len(s))