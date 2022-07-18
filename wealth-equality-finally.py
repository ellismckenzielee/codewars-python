## Wealth Equality, Finally! kata
## https://www.codewars.com/kata/5815f7e789063238b30001aa

def redistribute_wealth(wealth):
    average = sum(wealth) / len(wealth)
    for i in range(len(wealth)):
        wealth[i] = average
