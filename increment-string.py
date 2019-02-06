import re
def increment_string(strng):
    result = re.findall('(?<=\w)[\d]+$', strng)
    result = str(result)[2:-2]
    strng_list = list(strng)
    result_list = list(result)
    strng_contains_letters = any(c.isalpha() for c in strng)
    if result and strng_contains_letters == True:
        if result_list[-1] == '0':
            strng_list[-1] = '1'
            return ''.join(strng_list)
        
        elif '0' in result_list:
            for i in range(1, len(result_list)+1):
                if result_list[-i] == '0' and result_list[-i+1] !='0':
                    number = ''.join(result_list[-i+1:])
                    previous_number = int(number) 
                    new_number = previous_number+1
                    previous_number_string = str(previous_number)
                    new_number_string = str(new_number)
                    if len(new_number_string) != len(previous_number_string):
                        result_list[-i:] = list(new_number_string)
                        new_result = strng_list[0:-len(result_list)]
                        for number in result_list:
                            new_result.append(number)
                        return ''.join(new_result)
                    else: 
                        result_list[-i+1:] = list(new_number_string)
                        new_result = strng_list[0:-len(result_list)]
                        for number in result_list:
                            new_result.append(number)
                        return ''.join(new_result)
        
        else:
            previous_number = int(''.join(result_list))
            new_number = previous_number +1 
            new_number = list(str(new_number))
            new_result = strng_list[:-len(result_list)]
            for number in new_number:
                new_result.append(number)
            
            return ''.join(new_result)
                        
    elif strng == '':
        return '1'
        
    elif strng.isdigit():
        num_zeros = 0
        for i in strng:
            if i == '0':
                num_zeros = num_zeros + 1
            elif i != '0':
                break
        old_value = str(int(strng))
        new_value = str(int(strng)+1)
        if strng[0] == '0':
            if len(new_value) > len(old_value):
                return '0'*(num_zeros -1) + new_value
            else:
                if '0' in old_value:
                    return '0'*(num_zeros) + new_value
                else:
                    return '0'*(num_zeros) + new_value
        else:
            return str(int(old_value)+1)
    else: 
        output = list(strng)
        output.append('1')
        return ''.join(output)
            