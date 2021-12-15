# Closest distance between two not empty sets
from math import sqrt


min_dist = 9999999


def mass_center(pos1, mass1, pos2, mass2):
    pos = ((pos1[0] * mass1 + pos2[0] * mass2) / (mass1 + mass2), (pos1[1] * mass1 + pos2[1] * mass2) / (mass1 + mass2))
    mass = mass1 + mass2
    return pos, mass


def closest_mass_center(POS, M, pos1=(0, 0), mass1=0, pos2=(0, 0), mass2=0, step=0, curr_min=9999):
    if mass1 != 0 and mass2 != 0:
        dist = sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
        global min_dist
        min_dist = min(dist, min_dist)
    if step >= len(POS):
        return 0

    new_pos1, new_mass1 = mass_center(pos1, mass1, POS[step], M[step])
    new_pos2, new_mass2 = mass_center(pos2, mass2, POS[step], M[step])

    closest_mass_center(POS, M, new_pos1, new_mass1, pos2, mass2, step + 1)
    closest_mass_center(POS, M, pos1, mass1, new_pos2, new_mass2, step + 1)
    closest_mass_center(POS, M, pos1, mass1, pos2, mass2, step + 1)


pos = [(1, 1), (2, 2)]
mass = [1, 1]
closest_mass_center(pos, mass)
print(min_dist)