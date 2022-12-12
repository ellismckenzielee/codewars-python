# Lambda as a Mechanism for Open and Closed kata
# https://www.codewars.com/kata/53574972e727385ad10002ca/train/python

spoken    = lambda greeting: greeting.title() + '.'
shouted   = lambda greeting: greeting.upper() + '!'
whispered = lambda greeting: greeting.lower() + '.'

greet = lambda style, msg: style(msg)
