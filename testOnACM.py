# coding=utf-8
import collections
INF = 100000000000

class edge:
    def __init__(self, flow=0, cup=0, first=None, second=None):
        self.first = first
        self.second = second
        self.flow = flow
        self.cup = cup

class Dinica:
    def __init__(self, G, n, start, finish):
        self.n = n
        self.maxFlow = 0
        self.start = start
        self.finish = finish
        self.p = []
        self.d = []
        self.graph = G  # [[edge x n] x n]

    def bfs(self):
        self.d = [INF for i in range(self.n)]
        self.d[self.start] = 0
        q = collections.deque()
        q.append(self.start)
        while q:
            u = q.popleft()
            for v in range(len(self.graph[u])):
                if self.graph[u][v].flow < self.graph[u][v].cup and self.d[v] == INF:
                    self.d[v] = self.d[u] + 1
                    q.append(v)
        return self.d[self.finish] != INF

    def dfs(self, u, flow):
        if u == self.finish or flow == 0:
            return flow
        while self.p[u] < self.n:
            v = self.p[u]
            if self.d[v] == self.d[u] + 1:
                delta = self.dfs(v, min(flow, self.graph[u][v].cup - self.graph[u][v].flow))
                if delta:
                    self.graph[u][v].flow += delta
                    self.graph[v][u].flow -= delta
                    return delta
            self.p[u] += 1
        return 0

    def findMaxFlow(self):
        while self.bfs():  # пересчитываем d[i], проверяем достижима ли t из s
            self.p = [0 for i in range(self.n)]
            flow = self.dfs(self.start, INF)
            while flow != 0:
                self.maxFlow += flow
                flow = self.dfs(self.start, INF)
        return self.maxFlow

def readAdjacencyListToMatrix():
    n, m = map(int, input().split())
    M = [[0 for y in range(n)] for x in range(n)]
    for i in range(m):
        x, y, c = map(int, input().split())
        M[x - 1][y - 1] = c
    return M

def initGraphFromMatrix(M):
    n = len(M)
    G = [[edge(cup=M[x][y]) for y in range(n)] for x in range(n)]
    return G

M = readAdjacencyListToMatrix()
G = initGraphFromMatrix(M)
print(Dinica(M, len(M), 0, len(M) - 1).findMaxFlow())