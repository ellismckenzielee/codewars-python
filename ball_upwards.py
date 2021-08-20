#ball upwards kata
#https://www.codewars.com/kata/566be96bb3174e155300001b

def max_ball(v0):
    previous_max = 0 
    current = 1
    t = 0
    while current >= previous_max:
        t+=1
        current = (v0*t/(3.6*10)) - (0.5*9.81*(t/10)**2)
        if current > previous_max:
            previous_max = current
        else:
            print(t)
            return int(t-1)