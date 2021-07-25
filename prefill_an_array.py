#Prefill an array kata
#https://www.codewars.com/kata/54129112fb7c188740000162

def prefill(n,v='undefined'):
    try:
        return [v] * int(n)
    except:
        raise TypeError(f'{n} is invalid')
    