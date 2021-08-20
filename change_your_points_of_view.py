#change your points of view kata
#https://www.codewars.com/kata/5ca3ae9bb7de3a0025c5c740

def point(a, b):
    list = [a,b]
    return lambda c : list[c]
    
def fst(pt):
    #Returns x coordinate
    return pt(0)
    
def snd(pt):
    #Returns y coordinate
    return pt(1)
    
def sqr_dist(pt1, pt2):
    #Returns square of distance
    x1 = fst(pt1)
    x2 = fst(pt2)
    y1 = snd(pt1)
    y2 = snd(pt2)
    
    return ((x2-x1)**2 + (y2-y1)**2)
    
def line(pt1, pt2):
    x1 = fst(pt1)
    x2 = fst(pt2)
    y1 = snd(pt1)
    y2 = snd(pt2)
    m = -(y2-y1)/(x2-x1)
    y_coeff = 1
    c = -(y1+(x1*m))
    return [round(m*(x2-x1)), round(y_coeff*(x2-x1)), round(c*(x2-x1))]