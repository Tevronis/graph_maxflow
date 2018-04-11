import generator
from algorithms.pushFlow import PushFlow
import matplotlib.pyplot as plt
from graph import Graph
from ui.graphViz import GraphViz

n = 4
m = 5
s = 0
t = n - 1


def main():
    M = generator.GraphGenerator(7, 10)

    M = next(M)
    # M = readMatrix()
    M = Graph.readMatrixFromFile('input')

    print("Push Flow")
    #print("Dinica")
    G = Graph.initGraphFromMatrix(M)
    pf = PushFlow(G, len(M), s, t)
    pf.findMaxFlow()
    pf.printFlow()
    pf.printCup()
    print(pf.getMaxFlow())

    gv = GraphViz(G)
    gv.draw()

    plt.show()


main()
