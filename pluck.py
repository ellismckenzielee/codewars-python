#pluck kata
#https://www.codewars.com/kata/530017aac7c0f49926000084

def pluck(objs, name): 
    output = []
    for obj in objs:
        if name in obj:
            output.append(obj[name])
        else:
            output.append(None)
    return output