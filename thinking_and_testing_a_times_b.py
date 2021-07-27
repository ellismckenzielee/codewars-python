#Thinking & Testing: A * B kata
#https://www.codewars.com/kata/5a90c9ecb171012b47000077

def test_it(a, b):
    a = list(map(int, list(str(a))))
    b = list(map(int, list(str(b))))
    total = 0
    for numa in a:
        for numb in b:
            total += numa*numb
    return total