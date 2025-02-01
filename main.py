import random
import numpy as np


def generate_matrix(cols, rows):
    res = []
    for col in range(cols):
        for row in range(rows):
            if row == col:
                res[col][row] = 0
            else:
                res[col][row] = random.randint(1, 1000)
    return res


def get_txt_matrix(file_name):
    with open('tests/' + file_name) as f:
        lines = (line for line in f if not line.startswith('#'))
        FH = np.loadtxt(lines, delimiter=',', skiprows=2)
        return


print(get_txt_matrix("hospital_data_set.txt"))
