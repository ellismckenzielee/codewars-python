###Unary Messages - codewars kata 
###https://www.codewars.com/kata/5e5ccbda30e9d0001ec77bb6
###See link for description

def send(s):
    output = ''
    concat_s = ''
    for letter in s:
        letter = bin(ord(letter)).split('b')[1]
        if len(letter) <=6:
            concat_s += '0'
        concat_s += letter
    s = concat_s
    
    counts = []
    digit = []
    count = 0
    previous = concat_s[0]
    print(concat_s)
    for num in concat_s:
        if num == previous:
            count += 1
        else:
            counts.append(count)
            count = 1
            if num == '0':
                digit.append('1')
                previous = '0'
            elif num == '1':
                digit.append('0')
                previous = '1'
    digit.append(previous)
    counts.append(count)
    for i, digit in enumerate(digit):
        if digit == '1':
            output += ' 0 ' + '0'*counts[i]
        else:
            output += ' 00 ' + '0'*counts[i]
    return output.strip()
         

def receive(s):
    split = s.split(' ')
    nums = split[0::2]
    counts = split[1::2]
    binary = list(map(num_sorter, list(zip(nums,counts))))
    binary = ''.join(binary)
    letters_split = [binary[i:i+7] for i in range(0, len(binary), 7)]
    output = ''
    for letter in letters_split:
        output += chr(int(letter, base=2))
    return output
  
def num_sorter(x):
    if x[0] == '0':
        return '1'*len(x[1])
    else:
        return '0'*len(x[1])