import time

from defines import *
from algorithms import MaxFlowAlgo


class PushFlow(MaxFlowAlgo):

    def __init__(self, G, n, start, finish):
        super().__init__(G, n, start, finish)
        self.high = [0 for _ in range(n)]
        self.e = [0 for _ in range(n)]
        self._time_start = time.time()
        self.findMaxFlow()
        self.time = time.time() - self._time_start

    def __push(self, u, v):
        d = min(self.e[u], self.graph[u][v].cup - self.graph[u][v].flow)
        self.graph[u][v].flow += d
        self.graph[v][u].flow = -self.graph[u][v].flow
        self.e[u] -= d
        self.e[v] += d


    def __lift(self, u):
        d = INF
        for i in range(self.n):
            if self.graph[u][i].cup - self.graph[u][i].flow > 0:
                d = min(d, self.high[i])

        if d == INF:
            return
        self.high[u] = d + 1

    def findMaxFlow(self):
        for i in range(1, self.n):
            self.e[i] = self.graph[0][i].cup
            self.graph[0][i].flow = self.graph[0][i].cup
            self.graph[i][0].flow = -self.graph[0][i].cup
        self.high[0] = self.n

        while True:
            i = 1
            n = self.n
            while i < n - 1:
                if self.e[i] > 0:
                    break
                i += 1
            if i == n - 1:
                break

            j = 0
            while j < n:
                if self.graph[i][j].cup - self.graph[i][j].flow > 0 and self.high[i] == self.high[j] + 1:
                    break
                j += 1

            if j < n:
                self.__push(i, j)
            else:
                self.__lift(i)

        for i in range(n):
            if self.graph[0][i].cup:
                self.maxFlow += self.graph[0][i].flow

        return self.maxFlow

