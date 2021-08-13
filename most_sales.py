#most sales kata
#https://www.codewars.com/kata/5e16ffb7297fe00001114824

def top3(products, amounts, prices):
    totals = list(map(lambda x: x[0]*x[1], zip(amounts,prices)))
    ordered_products = []
    
    for i in range(0,3):
        max_index = totals.index(max(totals))
        ordered_products.append(products[max_index])
        totals[max_index] = -1
    return ordered_products