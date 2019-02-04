def is_valid_IP(strng):
    '''Function checks the validity of IP address'''
    list = strng.split('.')
    print(list)
    if len(list) == 4:
        for item in list:
            if item[0] == '0' and len(item) > 1:
                return False
            elif not item.isalnum():
                return False
            elif not item.isnumeric():
                return False
            elif int(item) < 0 or int(item) > 255:
                return False
        return True
    else:
        return False