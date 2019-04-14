import numpy as np
def yoga(classroom, poses):
    '''Return amount of poses a yoga class can perform based on given criteria'''
    if classroom == [] or poses == []:
        return 0
    classroom = np.array(classroom)
    total_poses = 0
    for row in classroom:
        row_total = sum(row)
        row += row_total
        for pose in poses:
            total_poses += np.sum([pose <= row])
    return total_poses