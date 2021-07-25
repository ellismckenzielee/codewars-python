#Most Frequent Weekdays kata
#https://www.codewars.com/kata/56eb16655250549e4b0013f4

from datetime import date 
def most_frequent_days(year):
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start = date(year,1,1).weekday()
    end = date(year, 12, 31).weekday()
    days = list(range(start, 7)) + list(range(0 ,end +1))
    total = days.count(max(days,key=days.count))
    result = []
    for day in [0,1,2,3,4,5,6]:
        if day in days:
            if days.count(day) == total:
                result.append(day)
    return list(map(lambda x: names[x], result))
                    