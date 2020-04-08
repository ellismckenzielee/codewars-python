from datetime import datetime, timedelta
def half_life(person1, person2):
    year, month, day = list(map(int, person1.split('-')))
    person1 = datetime(year,month,day)

    year, month, day = list(map(int, person2.split('-')))
    person2 = datetime(year,month,day)
    
    ans = (max(person1, person2) + timedelta(days=abs(person2-person1).days))
    return ans.strftime('%Y-%m-%d')