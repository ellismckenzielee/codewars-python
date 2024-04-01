# Find the discounted prices kata
# https://www.codewars.com/kata/56f3ed90de254a2ca7000e20/train/python/6609b40e0902b101b932c149
def find_discounted(prices):

    if prices == "":
        return ""
    
    prices = list(map(int, prices.split(' ')))
    n = len(prices)
    
    if 0 in prices:
        return '0'
    
    initial_prices = []
    
    for price in prices:
        initial_prices.append(price / 0.75)
    
    discounted_prices = []
    while len(discounted_prices) < n/2:
        initial_price = initial_prices.pop(0)
        if initial_price in prices:
            index = prices.index(initial_price)
            prices.pop(index)
            
            # remove the initial_price calculated from 
            # the price just removed
            index = initial_prices.index(initial_price / 0.75)
            initial_prices.pop(index)
            
            discounted_prices.append(int(initial_price * 0.75))
            
    return ' '.join(map(str,discounted_prices))
        
