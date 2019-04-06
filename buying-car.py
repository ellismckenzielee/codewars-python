import math
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    '''Function calculates how many months to afford a car, based on
    car prices and devaluation'''
    old_car_value = startPriceOld
    new_car_value = startPriceNew
    total_money = 0
    afford = False
    months = 1
    car_montly_loss = percentLossByMonth
    if old_car_value >=new_car_value:
        return [0, old_car_value - new_car_value]
        
    while afford == False:
        if months % 2 == 0 and months != 0:
            car_montly_loss += 0.5
        old_car_value = old_car_value - (old_car_value*car_montly_loss/100)
        new_car_value = new_car_value - (new_car_value*car_montly_loss/100)
        total_money = old_car_value +(savingperMonth*months)
        if total_money >= new_car_value:
            return [months, round(total_money-new_car_value, 0)]
        months += 1