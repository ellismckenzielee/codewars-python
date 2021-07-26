#Data Reverse kata
#https://www.codewars.com/kata/569d488d61b812a0f7000015

def data_reverse(data):
    bytes = []
    for i in range(len(data), -1, -8):
        bytes.extend(data[i:i+8])
    return bytes   