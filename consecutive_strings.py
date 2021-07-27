#consecutive strinngs kata
#https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):
    concat, longest, output = [],0,''
    if k > 0 and k <= len(strarr):
        for i in range(len(strarr[:])):
            concat.append(''.join(strarr[i:i+k]))
            if len(concat[-1]) > longest:
                output = concat[-1]
                longest = len(concat[-1])
    return output
