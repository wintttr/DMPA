import math
import numpy as np


def gaussian_func(x, y, a, b, sigm):
    k = 1 / (2 * math.pi * math.pow(sigm, 2))
    e_power = -(math.pow(x - a, 2) + math.pow(y - b, 2)) / (2 * math.pow(sigm, 2))
    return k * math.exp(e_power)


def create_gaussian_matrix(d, sigm):
    if d % 2 != 1:
        raise Exception("Размерность - чётное число")

    result = np.zeros((d, d))
    a = d // 2

    for i in range(0, d):
        for j in range(0, d):
            result[i, j] = gaussian_func(i, j, a, a, sigm)

    return result
