#Weather prediction kata
#https://www.codewars.com/kata/602d1d769a1edc000cf59e4c

'''
Parameters:

 - days (n) number of days for prediction, an integer
 - weather_today (i), an integer
 - final_whether (j) we want to predict in n days, an integer
 - P = [[p_11, ..., p_1k], [p_21, ..., p_2k], ..., [p_k1, ..., p_kk]],
   tranistion matrix, where p_xy is probability going from weather x to y in one day
'''
import numpy as np
def weather_prediction(days, weather_today, final_weather, P):
    trans = np.matrix(P)
    current = np.zeros(len(P))
    current[weather_today]= 1
    for i in range(days):
        current = current*trans
    return current[0, final_weather]