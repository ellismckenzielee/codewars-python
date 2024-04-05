# Longest Mountain Pass kata
# https://www.codewars.com/kata/660595d3bd866805d00ec4af
def longest_mountain_pass(mountains, E):
    if not mountains:
        return (0, 0)
    n = len(mountains)
    start, end, distance, max_distance = 0, 1, 1, 1
    start_max_distance = 0
    current_energy = E
    energies_added = []
    while end < n:
        energy_required = max(mountains[end] - mountains[end - 1], 0)
        if end == start:
            energy_required = 0
        if energy_required <= current_energy:
            current_energy -= energy_required
            distance += 1
            if distance > max_distance:
                max_distance = distance
                start_max_distance = start            
            
            energies_added.append(energy_required)
            
            end += 1

        elif energy_required > current_energy:
            if start == end:
                start += 1
                end += 1
                distance = 1
            else:
                start += 1
                if energies_added:
                    tail_energy = energies_added.pop(0)
                    current_energy += tail_energy
                distance -= 1
    return (max_distance, start_max_distance if start_max_distance else 0 )
