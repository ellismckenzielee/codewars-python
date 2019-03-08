def basic_op(operator, value1, value2):
    '''Outputs a value based upon the operator provided'''
    outputs = {
    '+': value1 + value2,
    '-': value1 - value2,
    '*': value1 * value2,
    '/': value1 / value2
    }
    return outputs[operator]