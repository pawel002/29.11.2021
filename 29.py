# center of mass of 3 points is in distance r from (0,0,0)
# FOR METHOD
from math import sqrt


def mass_center(pos1, pos2, pos3, mass1, mass2, mass3):
    x = pos1[0] * mass1 + pos2[0] * mass2 + pos3[0] * mass3
    y = pos1[1] * mass1 + pos2[1] * mass2 + pos3[1] * mass3
    z = pos1[2] * mass1 + pos2[2] * mass2 + pos3[2] * mass3
    mass = mass1 + mass2 + mass3
    return (x, y, z), mass


def center_of_mass(POS, M, r):
    L = len(POS)
    for i in range(L):
        for j in range(i, L):
            for k in range(j, L):
                if i != j and j != k and k != i:
                    pos, mass = mass_center(POS[i], POS[j], POS[k], M[i], M[j], M[k])
                    if sqrt(pos[0] ** 2 + pos[1 ** 2 + pos[2] ** 2]) <= r:
                        return True
    return False

# P - position arr
# M - mass arr
# center_of_mass(P, M, r)
