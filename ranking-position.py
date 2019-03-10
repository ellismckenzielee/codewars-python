def ranking(people):
    '''Rank people based on score and name, and then return as a list of dictionaries'''
    points_scores = {}
    scores = []
    for person in people:
        if person['points'] in scores:
            points_scores[person['points']].append(person['name'])
        else:
            points_scores[person['points']] = [person['name']]
            scores.append(person['points'])
    
    output_list = []
    output_dict = {}
    counter = 1
    for score in sorted(scores)[::-1]:
        if len(points_scores[score]) == 1:
            output_dict = {'name': points_scores[score][0], 'points': score, 'position': counter}
            output_list.append(output_dict)
            counter += 1
        else:
            for name in sorted(points_scores[score]):
                output_dict = {'name': name, 'points': score, 'position': counter}
                output_list.append(output_dict)
            counter += len(points_scores[score])
    return output_list