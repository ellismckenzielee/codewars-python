#decode the QR code kata
#https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f

import numpy as np
def scanner(qrcode):
    qr_code_indeces = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for i in range(21)]
    for i, row in enumerate(qrcode):
        for j, val in enumerate(row):
            if  (i+j)% 2 == 0:
                val = 1 - val
            qr_code_indeces[i][j] = val
    qr_code = np.array(qr_code_indeces)
    qr_code = qr_code[9:]
    odd, output = 0, []
    for i in [19, 17, 15, 13]:
        columns = qr_code[:,[i, i + 1]]
        if odd == 1:
            direction = 1
        else:
            direction = -1
            
        for row in columns[::direction]:
            output += row.tolist()[::-1]
        odd = 1 - odd
    output = ''.join(list(map(str,output[4:])))
    letter_count = int(output[:8], 2)
    output = output[8:]
    word = ''
    print(letter_count)
    for i in range(0, (letter_count * 8) + 11, 8):
        word += chr(int(output[i:i+8], 2))
        if len(word) == letter_count:
            return word

    