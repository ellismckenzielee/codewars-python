#write out expression! kata
#https://www.codewars.com/kata/57e2afb6e108c01da000026e

def expression_out(exp):
    operators = { '+':   'Plus ',
                  '-':   'Minus ',
                  '*':   'Times ',
                  '/':   'Divided By ',  
                  '**':  'To The Power Of ',
                  '=':   'Equals ',
                  '!=':  'Does Not Equal ' }
    nums = {
        '1':    'One',
        '2':    'Two',
        '3':    'Three',
        '4':    'Four',
        '5':    'Five',
        '6':    'Six',
        '7':    'Seven',
        '8':    'Eight',
        '9':    'Nine',
        '10': 'Ten'
    }
    num1, op, num2 = exp.split(' ')
    return nums[num1] + ' ' + operators[op] + nums[num2] if op in operators else 'That\'s not an operator!'