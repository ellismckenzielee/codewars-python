##LAST DIGIT TO APPEAR IN SEQUENCE OF POWERS KATA
##Code below returns the last digit to appear in a 
##sequence of powers (n)

def LDTA(n):
    num_set = set()
    power = 1
    counter = 0
    while counter < 100:
        total = n**power
        ints = list(map(int, list(str(total))))
        for num in ints:
            if num not in num_set:
                if len(num_set) == 9:
                    return num
                else:
                    num_set.add(num)
        counter += 1
        power += 1