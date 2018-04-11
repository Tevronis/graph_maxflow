# coding=utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from graph import Graph
from algorithms.pushFlow import PushFlow
from ui import design
from properties import s, t
from ui.graphViz import GraphViz
import matplotlib.pyplot as plt


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        grid = QGridLayout()
        self.setLayout(grid)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 1, 9, 9)
        print(self.listWidget.selectedItems())
        self.executeBtn.clicked.connect(self.handler_push_flow)

    def handler_push_flow(self):
        for item in self.listWidget.selectedItems():
            print(item)
        self.figure.clf()
        M = Graph.readMatrixFromFile('input')
        G = Graph.initGraphFromMatrix(M)
        pf = PushFlow(G, len(M), s, t)
        pf.findMaxFlow()
        pf.printFlow()
        pf.printCup()
        print(pf.getMaxFlow())

        gv = GraphViz(G)
        plt.axis('off')
        gv.draw()
        self.canvas.draw_idle()

    def handler_dinica(self):
        self.figure.clf()
        M = Graph.readMatrixFromFile('input')
        G = Graph.initGraphFromMatrix(M)
        pf = PushFlow(G, len(M), s, t)
        pf.findMaxFlow()
        pf.printFlow()
        pf.printCup()
        print(pf.getMaxFlow())

        gv = GraphViz(G)
        plt.axis('off')
        gv.draw()
        self.canvas.draw_idle()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
