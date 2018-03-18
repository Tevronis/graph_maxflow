# 1kkk

class edge:
    def __init__(self, flow=0, cup=0, first=None, second=None):
        self.first = first
        self.second = second
        self.flow = flow
        self.cup = cup


def printMatrix(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=' ')
        print()
