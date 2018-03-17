import generator
from dinica import Dinica
from pushFlow import PushFlow
import networkx as nx
import matplotlib.pyplot as plt
import utils


def readMatrix():
    n = int(input())
    M = [[0 for y in range(n)] for x in range(n)]
    for i in range(n):
        M[i] = list(map(int, input().split()))
    return M


def readAdjacencyListToMatrix():
    n, m = map(int, input().split())
    M = [[0 for y in range(n)] for x in range(n)]
    for i in range(m):
        x, y, c = map(int, input().split())
        M[x - 1][y - 1] = c
    return M


def initGraphFromMatrix(M):
    n = len(M)
    G = [[utils.edge(cup=M[x][y]) for y in range(n)] for x in range(n)]
    return G


def initGraphFrom():
    pass


def initGraph(n):
    G = [[utils.edge() for y in range(n)] for x in range(n)]
    G[0][1].cup = 3
    G[1][3].cup = 1
    G[0][2].cup = 1
    G[2][3].cup = 2
    G[1][2].cup = 1
    return G


def main():
    n = 4
    m = 5
    s = 0
    t = n - 1

    # M = readAdjacencyListToMatrix()
    # M = readMatrix()
    M = generator.GraphGenerator(10, 10)

    M = next(M)
    M = initGraph(4)
    DG = nx.DiGraph()
    for i in range(len(M)):
        for j in range(len(M)):
            print(M[i][j].cup, end=' ')
            if M[i][j].cup > 0:
                DG.add_weighted_edges_from([(i, j, M[i][j].cup)])
        print('\n')
    nx.draw(DG, with_labels=True, font_weight='bold')
    plt.show()
    return
    G = initGraphFromMatrix(M)
    flow = PushFlow(G, len(M), s, t).findMaxFlow()
    print(flow)

    G = initGraphFromMatrix(M)
    flow = Dinica(G, len(M), s, len(M) - 1).findMaxFlow()
    print(flow)

main()
