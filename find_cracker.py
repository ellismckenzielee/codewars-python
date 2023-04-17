# Find Cracker kata
# https://www.codewars.com/kata/59f70440bee845599c000085

weightings = {
    "A": 30,
    "B": 20,
    "C": 10,
    "D": 5
}

def is_hacked(result):
    name, total_score, scores = result
    high_grades = list(filter(lambda x: x in ['A', 'B'], scores))
    bonus = len(high_grades) > 4 and len(high_grades) == len(scores)
    total = sum(map(lambda x: weightings[x] if x in weightings else 0, scores)) 
    total += (20 if bonus else 0)
    if total > 200:
        total = 200
    return total != total_score

def find_hack(arr):
    hacked_results = filter(is_hacked, arr)
    return list(map(lambda result: result[0], hacked_results))
