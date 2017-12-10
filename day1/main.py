import numpy as np

def solve():
    input = day1Input.strip().split(', ')
    position = 0 + 0j
    direction = 0 + 1j
    QG = None
    grille = np.ndarray((2000,2000))
    grille[0][0] = 1

    for order in xrange(0, len(input)):
        dist = int(input[order][1:])
        if input[order][0] == 'R':
            direction *= -1j
        else:
            direction *= 1j
        for step in xrange(0, dist):
            position += direction
            grille[int(position.real)][int(position.imag)] += 1
            if grille[int(position.real)][int(position.imag)] > 1 and QG is None:
                QG = int(abs(position.real) + abs(position.imag))


    return int(abs(position.real) + abs(position.imag)), QG



day1Input = open("day1/input.txt", "r").read()
