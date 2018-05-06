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
        self._used = []

    def switchToMatrix(self):
        self.mode = MATRIX

    def switchToList(self):
        self.mode = LIST

    def gen_matrix(self):
        def get_indexes():
            x, y = 0, 0
            while x == y and not (x, y) in self._used:
                x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            self._used.append((x, y))
            return x, y

        result = [[0 for x in range(self.n)] for y in range(self.n)]
        for x in range(self.m):
            idx, jdx = get_indexes()
            result[idx][jdx] = self.generate_cup(idx, jdx)
        return result

    def check_way(self, M):
        if M is None: return False

        length = [0]

        def dfs(u, d, length):
            if u == len(M) - 1:
                length[0] = d
            used[u] = True
            for to in range(self.n):
                if not used[to] and M[u][to]:
                    dfs(to, d + 1, length)

        used = [False for i in range(self.n)]
        dfs(0, 0, length)
        if used[len(M) - 1] and length[0] > len(M) // 3:
            return True
        return False

    def gen(self):
        result = None
        while not self.check_way(result):
            result = self.gen_matrix()
        log_report('Generate graph:\n', matrix_to_str(result))
        return result

    def generate_cup(self, x, y):
        return random.randint(0, self.max_cup)

    def __next__(self):
        return self.gen()
