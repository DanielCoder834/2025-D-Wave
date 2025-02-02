import os
import pathlib
import random
import numpy as np
import resources
# https://github.com/dwave-examples/job-shop-scheduling-cqm/blob/main/src/job_shop_scheduler.py
# pip install dwave-ocean-sdk
from dimod import ConstrainedQuadraticModel


def string_to_matrix(string):
    matrix = [row.split() for row in string.split("\n")]
    res = []
    for arr in matrix:
        res.extend(arr)
    return np.matrix(res, dtype=int)


class CQM:
    def __init__(self, rooms_per_floor, elem_count, d_matrix, flow_matrix):
        self.height_line = []
        self.make_height_line(rooms_per_floor)
        print(self.height_line)
        self.cqm = ConstrainedQuadraticModel()
        # print(dir(self.cqm.variables))
        # self.cqm.set_objective()
        self.yj = []
        self.month = 0
        self.max_val = 100
        self.dmn = d_matrix
        self.flow = flow_matrix
        self.bits = np.random.randint(
            0, 1, size=(elem_count, elem_count))
        # N = 19

        # self.cqm.add_constraint(
        #     sum(self.yj) + (sum(self.yj)**2) - 1938
        #     == 0,
        #     label="Math works out",
        # )
        self.alpha = 1
        self.beta = 1
        self.gamma = 1
        self.cost = []
        for j in range(elem_count):
            for k in range(elem_count):
                # difference in floors
                # dist = self.yj
                # print(j, k)
                # self.c += self.f[j, k] * self.d[y[j], y[k]] + self.alpha * self.d[y[j], y[k]] \
                #     + self.beta * self.f[j, k] * \
                #     self.f[j, k] + self.gamma * self.h()
                # self.cqm.set_objective(sum(self.yj)**2)

    def make_height_line(self, rooms_per_floor):
        last_elem = 0
        heights_diffs = []
        for i in range(len(rooms_per_floor)):
            heights_diffs.append(rooms_per_floor[i] + last_elem)
            last_elem = rooms_per_floor[i]
        heights_diffs[len(rooms_per_floor) - 1] += last_elem
        height_idx = 1
        room_idx = 0
        max_rooms = heights_diffs[0]
        while height_idx < heights_diffs[len(heights_diffs) - 1]:
            self.height_line.append(room_idx)
            if (height_idx >= max_rooms):
                room_idx += 1
                max_rooms = heights_diffs[room_idx]
            height_idx += 1
        self.height_line.append(room_idx)

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
    cqm = CQM([2, 2, 2], 25, resources.D_matrix, resources.F_matrix)
    first, last = cqm.get_txt_matrix("hospital_data_set.txt")
