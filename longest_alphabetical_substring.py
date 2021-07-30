#longest alphabetic substring kata
#https://www.codewars.com/kata/5a7f58c00025e917f30000f1

import re
def longest(s):
    matches = re.findall('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*', s)
    current_longest = matches[0]
    for match in matches:
        if len(match) > len(current_longest):
            current_longest = match
    return current_longest 