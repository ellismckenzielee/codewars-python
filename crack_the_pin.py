#crack the pin kata
#https://www.codewars.com/kata/5efae11e2d12df00331f91a6

import hashlib, itertools
def crack(hash):
    result = hashlib.md5('00078'.encode())
    for pin in itertools.product(range(10), repeat=5):
        pin = ''.join(list(map(str, pin)))
        result = hashlib.md5(pin.encode()).hexdigest()

        if result == hash:
            return pin
