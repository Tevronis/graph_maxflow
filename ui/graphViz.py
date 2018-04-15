import itertools

import networkx as nx
import matplotlib.pyplot as plt


class GraphViz:
    def __init__(self, G, only_way=False):
        self.G = G
        self.DG = nx.DiGraph()
        self.edge_colors = []
        self.node_pos = {}
        self.ONLY_WAY = only_way
        self.n = len(G)
        self.__init_graph()
        self.edge_labels = nx.get_edge_attributes(self.DG, 'route')
        self.pos = nx.shell_layout(self.DG)

    def __init_graph(self):
        def get_indexes(n):
            for i in range(n):
                for j in range(n):
                    yield i, j
        if self.ONLY_WAY:
            [self.__initEdge(i, j, self.G[i][j].flow, self.G[i][j].cup) for i, j in
             get_indexes(self.n) if self.G[i][j].cup > 0 and self.G[i][j].flow > 0]
        else:
            [self.__initEdge(i, j, self.G[i][j].flow, self.G[i][j].cup) for i, j in
             get_indexes(self.n) if self.G[i][j].cup > 0]

    def __getEdgeColor(self, flow, cup):
        if flow == 0:
            return "#280000"
        elif flow < cup:
            return "#780000"
        else:
            return "#F80000"
        # "#F80000"

    def __drawEdges(self):
        nx.draw_networkx_edge_labels(self.DG, self.pos, edge_labels=self.edge_labels, clip_on=False)  # clip_on opt

    def __drawNodes(self):
        nx.draw_networkx_nodes(self.DG, self.node_pos)

    def draw(self):
        self.__drawEdges()
        nx.draw_shell(self.DG, with_labels=True, edge_color=self.edge_colors)

    def __initEdge(self, x, y, flow, cup):
        if self.G[y][x].cup > 0:
            edge_label = "{0}->{1}: {2}/{3}\n{1}->{0}: {4}/{5}".format(x, y, flow, cup, self.G[y][x].flow,
                                                                       self.G[y][x].cup)
        else:
            edge_label = "{0}/{1}".format(flow, cup)
        self.DG.add_edge(x, y, route=edge_label)
        self.edge_colors.append(self.__getEdgeColor(flow, cup))
