#dashatize it kata
#https://www.codewars.com/kata/58223370aef9fc03fd000071

def dashatize(num):
    output = ''
    for num in str(num):
        if num.isnumeric() and int(num) % 2 !=0:
            output += '-' + num + '-' 
        else:
            output += num
    return output.replace('--', '-').strip('-')