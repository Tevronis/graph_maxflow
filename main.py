import dinica
import pushFlow
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
    G = [[dinica.edge() for y in range(n)] for x in range(n)]
    G[0][1].cup = 3
    G[1][3].cup = 1
    G[0][2].cup = 1
    G[2][3].cup = 2
    G[1][2].cup = 1
    return G


def main():
    n = 4
    m = 5
    # G = initGraph(n)

    s = 0
    t = n - 1

    # pf = pushFlow.PushFlow(G, n, s, t)
    # print(pf.findMaxFlow())

    # G = initGraph(n)
    # dc = Dinica.Dinica(G, n, s, t)
    # print(dc.findMaxFlow())

    M = readAdjacencyListToMatrix()

    G = initGraphFromMatrix(M)
    flow = pushFlow.PushFlow(G, len(M), s, t).findMaxFlow()
    print(flow)

    G = initGraphFromMatrix(M)
    flow = dinica.Dinica(G, len(M), s, len(M) - 1).findMaxFlow()
    print(flow)

main()
