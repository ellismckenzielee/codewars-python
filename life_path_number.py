#Life path number kata 
#https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0

def life_path_number(birthdate):
    if type(birthdate[0]) != int:  
        num = list(filter(lambda x: x in '0123456789', list(birthdate)))
        num = list(map(int, num))
        return life_path_number(num)
    
    elif len(birthdate)> 1:
        total = sum(birthdate)
        total = list(map(int, str(total)))
        return life_path_number(total)
    else:
        return birthdate[0]