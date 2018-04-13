import itertools
import random

from defines import *
from utils import log_report, matrix_to_str


class GraphGenerator:
    def __init__(self, vertex_cnt, edges_cnt):
        self.n = vertex_cnt
        self.m = edges_cnt
        self.mode = MATRIX
        self.WITHOUT_NODE_LOOP = True
        self.max_cup = 20

    def switchToMatrix(self):
        self.mode = MATRIX

    def switchToList(self):
        self.mode = LIST

    def gen(self):
        def check_edges(value):
            if value:
                self.m -= 1
            if self.m == 0:
                return True
            return False
        result = [[0 for x in range(self.n)] for y in range(self.n)]
        is_generated = False
        while not is_generated:
            for idx, jdx in itertools.combinations(range(self.n), 2):   # without main horizontal
                isAdded, result[idx][jdx] = self.generate_cup(idx, jdx)
                if check_edges(isAdded):
                    break
            else:
                continue
            is_generated = True

        log_report('Generate graph:\n', matrix_to_str(result))
        return result

    def generate_cup(self, x, y):
        if x == y:
            return False, 0
        if random.randint(1, 20) > 18:
            return True, random.randint(0, self.max_cup)
        else:
            return False, 0

    def __next__(self):
        return self.gen()
