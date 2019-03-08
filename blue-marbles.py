def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    '''Returns probability of picking a blue based on the numbers pulled out of a bag previously'''
    return (blue_start-blue_pulled)/(blue_start-blue_pulled+red_start-red_pulled)