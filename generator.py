import random

from defines import *
from utils import edge


class GraphGenerator:
    def __init__(self, vertex_cnt, edges_cnt):
        self.n = vertex_cnt
        self.m = edges_cnt
        self.mode = MATRIX
        self.max_cup = 20

    def switchToMatrix(self):
        self.mode = MATRIX

    def switchToList(self):
        self.mode = LIST

    def gen(self):
        result = [[self.generate_cup() for y in range(self.n)] for x in range(self.n)]
        return result

    def generate_cup(self):
        if random.randint(1, 20) > 14:
            return random.randint(0, self.max_cup)
        else:
            return 0

    def __next__(self):
        return self.gen()
