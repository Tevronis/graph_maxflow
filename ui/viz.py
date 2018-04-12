# coding=utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import generator
from graph import Graph
from algorithms.pushFlow import PushFlow
from algorithms.dinica import Dinica
from ui import design
from properties import s, t
from ui.graphViz import GraphViz
import matplotlib.pyplot as plt


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        "Generate graph"
        "Alg push_flow"
        "Alg Dinica"
        "Draw Circle"
        "Draw"
        self.HANDLER_DICT = {"Alg Dinica": self.handler_dinica, "Alg push_flow": self.handler_push_flow,
                             "Generate": self.handler_generate_graph, "Draw Circle": self.handler_draw_circle,
                             "Draw": self.handler_draw}
        self.flow_algorithm = None
        grid = QGridLayout()
        self.setLayout(grid)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 1, 9, 9)
        print(self.listWidget.selectedItems())
        self.executeBtn.clicked.connect(self.handler_execute_from_listbox)

    def handler_execute_from_listbox(self):
        commands = []
        for item in self.listWidget.selectedItems():
            commands.append(item.text())
        for command in commands:
            self.HANDLER_DICT[command]()

    def get_matrix(self):
        M = generator.GraphGenerator(7, 10)
        M = next(M)
        #M = Graph.readMatrixFromFile('input')
        return M

    def handler_push_flow(self):
        M = self.get_matrix()
        G = Graph.initGraphFromMatrix(M)
        self.flow_algorithm = PushFlow(G, len(M), s, t)
        self.__draw(G)

    def handler_dinica(self):
        M = self.get_matrix()
        G = Graph.initGraphFromMatrix(M)
        self.flow_algorithm = Dinica(G, len(M), s, t)
        self.__draw(G)

    def __draw(self, G):
        self.figure.clf()
        gv = GraphViz(G)
        plt.axis('off')
        gv.draw()
        self.canvas.draw_idle()

    def handler_generate_graph(self):
        pass

    def handler_draw_circle(self):
        pass

    def handler_draw(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
