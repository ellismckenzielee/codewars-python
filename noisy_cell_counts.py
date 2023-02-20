# Noisy Cell Counts kata
# https://www.codewars.com/kata/63ebadc7879f2500315fa07e/train/python

def cleaned_counts(data):
    adjusted_data = [data[0]]
    for point in data[1:]:
        if point < adjusted_data[-1]:
            adjusted_data.append(adjusted_data[-1])
        else:
            adjusted_data.append(point)
    return adjusted_data
