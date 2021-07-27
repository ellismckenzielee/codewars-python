#Good vs Evil kata
#https://www.codewars.com/kata/52761ee4cffbc69732000738

def goodVsEvil(good, evil):
    good, evil = map(int, good.split(' ')), map(int, evil.split(' '))
    good_total = sum(map(lambda x: x[0]*x[1], zip(good, [1,2,3,3,4,10])))
    evil_total = sum(map(lambda x: x[0]*x[1], zip(evil, [1,2,2,2,3,5,10])))
    if good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    elif good_total < evil_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
    