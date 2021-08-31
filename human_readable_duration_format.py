#human readable duration format kata
#https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    years = int(seconds // (60*60*24*365))
    seconds -= years*(60*60*24*365)
    days = int((seconds // (60*60*24)))
    seconds -= days*(60*60*24)
    hours  = int(seconds// (60*60))
    seconds -= hours*(60*60)
    minutes = int(seconds//60)
    seconds -= minutes*60
    names = ['year', 'day', 'hour', 'minute', 'second']
    output = [] 
    for i,unit in enumerate([years, days, hours, minutes, seconds]):
        if unit > 1:
            output.append(str(unit) + ' ' + names[i] + 's')
        elif unit == 0:
            pass
        else:
            output.append((str(unit) + ' ' +  names[i]))
            
    if len(output) > 1:
        return ', '.join(output[0:-1]) + ' and ' + output[-1] 
    elif len(output) == 1:
        return output[0]
    else:
        return "now"
            