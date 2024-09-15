# Pointless Farmer
# https://www.codewars.com/kata/597ab747d1ba5b843f0000ca

def buy_or_sell(pairs, harvested_fruit):
    current_fruit = harvested_fruit
    trades = []
    for pair in pairs:
        if current_fruit in pair:
            index = pair.index(current_fruit)
            if index == 0:
                trades.append("buy")
            else:
                trades.append("sell")
            current_fruit = pair[1 - index]
        else:
            return "ERROR"
    return trades if current_fruit == harvested_fruit else "ERROR"
