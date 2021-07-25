#Some (but not all) kata
#https://www.codewars.com/kata/60dda5a66c4cf90026256b75

def some_but_not_all(seq, pred): 
    return len(list(filter(lambda x: pred(x), seq))) in  range(1, len(seq))