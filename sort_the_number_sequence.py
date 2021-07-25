#sort the number sequence kata
#https://www.codewars.com/kata/5816b76988ca9613cc00024f

def sort_sequence(sequence):
    output, temp = [], []
    for num in sequence:
        if num != 0:
            temp.append(num)
        else:
            output.append([sum(temp), sorted(temp)+[0]])
            temp = []
    output = sorted(output, key=lambda x: x[0])
    output = list(map(lambda x: x[1], output))
    return [item for sublst in output for item in sublst]
            
    