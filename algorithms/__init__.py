# coding=utf-8


class MaxFlowAlgo:
    def __init__(self, G, n, start, finish):
        self.n = n
        self.maxFlow = 0
        self.start = start
        self.finish = finish
        self.graph = G  # [[edge x n] x n]

    def findMaxFlow(self):
        pass

    def getGraph(self):
        return self.graph

    def printFlow(self):
        print('flow')
        n = self.n
        for i in range(n):
            for j in range(n):
                print(self.graph[i][j].flow, end=' ')
            print()

    def printCup(self):
        print('cup')
        n = self.n
        for i in range(n):
            for j in range(n):
                print(self.graph[i][j].cup, end=' ')
            print()

    def getMaxFlow(self):
        return self.maxFlow
