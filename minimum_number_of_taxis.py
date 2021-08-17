#minimum number of taxis kata
#https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d

import numpy as np 
def min_num_taxis(requests):
    start_times = [time[0] for time in requests]
    end_times = [time[1] for time in requests]
    earliest_time = min(start_times)
    latest_time = max(end_times)
    
    taxis = np.zeros(latest_time-earliest_time)
    for i, start_time in enumerate(start_times):
        taxis[start_time-earliest_time:end_times[i]-earliest_time+1] += 1
    return np.max(taxis)      