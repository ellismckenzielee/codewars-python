#regexp basics - is it a letter? kata
#https://www.codewars.com/kata/567de72e8b3621b3c300000b

def is_letter(s):
    print(s)
    return (ord(s.lower()) > 96 and ord(s.lower()) < 123)  if (s.isalnum() and len(s) == 1) else False