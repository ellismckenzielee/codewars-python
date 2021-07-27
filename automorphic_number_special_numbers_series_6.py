#automorphic number (special number series #6) kata
#https://www.codewars.com/kata/5a58d889880385c2f40000aa

def automorphic(n):
    n_squared = n**2
    return 'Automorphic' if str(n) == str(n_squared)[-len(str(n)):] else 'Not!!'
