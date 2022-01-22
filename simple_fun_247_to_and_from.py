## simple fun #247: to and from kata
## https://www.codewars.com/kata/590c3173cd3b99c467000a26

def to_and_from(a, b, t):
    distance = abs(a-b)
    modifier = 1
    if a-b > 0:
        modifier = -1
    if (t // distance)%2 == 0:
        return a + (t % distance*modifier)
    return b - (t % distance * modifier)