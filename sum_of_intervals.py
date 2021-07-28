#sum of intervals kata
#https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    output = set([])
    for interval in intervals:
        output.update(range(interval[0], interval[1]))
    return len(output)