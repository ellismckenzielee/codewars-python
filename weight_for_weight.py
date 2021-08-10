#weight for weight kata
#https://www.codewars.com/kata/55c6126177c9441a570000cc

def calc_weights(weight):
    total = 0
    for digit in weight:
        digit = int(digit)
        total += digit
    return total

def order_weight(strng):
    weights = strng.split(' ')
    weights_converted = list(map(calc_weights, weights))
    return ' '.join([x for _, x in sorted(zip(weights_converted, weights))])