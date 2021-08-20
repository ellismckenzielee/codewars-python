#loose change! kata
#https://www.codewars.com/kata/57e1857d333d8e0f76002169

money = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25,
    'dollar': 1
    }

def change_count(change):
    return "${:.2f}".format((sum([money[value] for value in change.split(' ')])))