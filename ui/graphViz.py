
import networkx as nx
import matplotlib.pyplot as plt

class GraphViz:
    def __init__(self, G):
        self.G = G
        self.DG = nx.DiGraph()
        self.edge_colors = []
        n = len(G)
        for i in range(n):
            for j in range(n):
                if G[i][j].cup > 0:
                    self.__initEdge(i, j, G[i][j].flow, G[i][j].cup)

        self.edge_labels = nx.get_edge_attributes(self.DG, 'route')
        self.pos = nx.spring_layout(self.DG)

    def __getEdgeColor(self, flow, cup):
        # power = int((flow / cup) * 10) + 1
        # return "#F" + str(power) + "0000"
        if flow == 0:
            return "#280000"
        elif flow < cup:
            return "#780000"
        else:
            return "#F80000"
        # "#F80000"

    def __drawEdges(self):
        nx.draw_networkx_edge_labels(self.DG, self.pos, edge_labels=self.edge_labels)

    def __drawNodes(self):
        pass

    def draw(self):
        self.__drawEdges()
        #nx.write_dot(G, 'multi.dot')
        nx.draw_circular(self.DG, with_labels=True, edge_color=self.edge_colors)
        #nx.draw_networkx(self.DG, self.pos, with_labels=True, edge_color=self.edge_colors)

    def __initEdge(self, x, y, flow, cup):
        if self.G[y][x].cup > 0:
            edge_label = "{0}->{1}: {2}/{3}\n{1}->{0}: {4}/{5}".format(x, y, flow, cup, self.G[y][x].flow, self.G[y][x].cup)
        else:
            edge_label = "{0}/{1}".format(flow, cup)
        self.DG.add_edge(x, y, route=edge_label)
        self.edge_colors.append(self.__getEdgeColor(flow, cup))
