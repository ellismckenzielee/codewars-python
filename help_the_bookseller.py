#help the bookseller! kata
#https://www.codewars.com/kata/54dc6f5a224c26032800005c

def stock_list(listOfArt, listOfCat):
    listOfArt =list(map(lambda x: (x.split(' ')[0][0], int(x.split(' ')[1])), listOfArt))
    totals = dict.fromkeys(listOfCat, 0)
    flag = True
    for lst in listOfArt:
        if lst[0] in listOfCat:
            totals[lst[0]] += lst[1]
            flag = False
    if flag == True:
        return ""
    return ' - '.join([f"({key} : {value})" for key, value in totals.items()])

