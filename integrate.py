def integrate(coefficient, exponent):
    '''Finds the coefficient and exponent of the integral of the input expression'''
    new_exponent = exponent + 1
    new_coeff = coefficient/(new_exponent)
    if new_coeff.is_integer():
        return str(int(new_coeff)) + 'x^' + str(new_exponent)
    return str(new_coeff) + 'x^' + str(new_exponent)