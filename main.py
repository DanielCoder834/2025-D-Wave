import os
import pathlib
import random
import numpy as np
# https://github.com/dwave-examples/job-shop-scheduling-cqm/blob/main/src/job_shop_scheduler.py
# pip install dwave-ocean-sdk
from dimod import ConstrainedQuadraticModel


def string_to_matrix(string):
    matrix = [row.split() for row in string.split("\n")]
    return np.matrix(matrix, dtype=int)


class CQM:
    def __init__(self):
        self.cqm = ConstrainedQuadraticModel()
        self.cqm.set_objective()
        self.yj = []
        self.month = 0

        # N = 19
        for i in range(19):
            self.yj.append(i)
        self.cqm.add_constraint(
            sum(self.yj) + (sum(self.yj)**2) - 1938
            == 0,
            label="Math works out",
        )
        self.alpha = 1
        self.beta = 1
        self.gamma = 1
        self.c = 0
        for j in range(19):
            for k in range(19):
                self.c += self.f[j, k] * self.d[y[j], y[k]] + self.alpha * self.d[y[j], y[k]] \
                    + self.beta * self.f[j, k] * self.f[j, k] + self.gamma * self.h() \
                    self.cqm.set_objective(sum(self.yj)**2)

    def generate_matrix(self, cols, rows):
        res = []
        for col in range(cols):
            for row in range(rows):
                if row == col:
                    res[col][row] = 0
                else:
                    res[col][row] = random.randint(1, 1000)
        return res

    def get_txt_matrix(self, file_name):
        file_path = 'tests/' + file_name
        with open(file_path) as f:
            _, first, last = f.read().split("\n\n")
            first_matrix = string_to_matrix(first)
            last_matrix = string_to_matrix(last)
            return first_matrix, last_matrix


# def build_cqm():
if __name__ == "__main__":
    first, last = get_txt_matrix("hospital_data_set.txt")
