#ski jump kata
#https://www.codewars.com/kata/57ed7214f670e99f7a000c73

def ski_jump(mountain):
    height = len(mountain)
    jump = (height * (height * 1.5) * 9)/10
    if jump < 10:
        sentence = 'He\'s crap!'
    elif jump < 25:
        sentence = 'He\'s ok!'
    elif jump < 50:
        sentence = 'He\'s flying!'
    else:
        sentence = 'Gold!!'
    return '{0:.2f}'.format(jump) + ' metres: ' + sentence