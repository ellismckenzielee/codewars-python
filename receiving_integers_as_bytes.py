#Receiving integers as bytes
#https://www.codewars.com/kata/56df605f2ebcd54c4d000335

def interpret_as_int32(stream):
    byte_string = b""
    output = []
    
    if not stream:
        return []
        
    for strng in stream:
        byte_string += strng
        
    for i in range(0, len(byte_string), 4):
        
        if len(byte_string[i:i+4]) < 4:
            continue
        result = int.from_bytes(byte_string[i:i+4], byteorder='big', signed=True)
        output.append(result)
        
    return output
        