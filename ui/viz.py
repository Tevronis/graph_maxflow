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
from ui.graphViz import GraphViz
from utils import log_report, clear_log, get_matrix_stats
import matplotlib.pyplot as plt


class ExampleApp(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.GENERATE = True
        self.HANDLER_DICT = {"Alg Dinica": self.handler_dinica,
                             "Alg push_flow": self.handler_push_flow,
                             "Generate mod": self.handler_generate_graph,
                             "File mod": self.handler_load_from_file,
                             "Generate next": self.handler_generate_next}
        self.flow_algorithm = None
        self.matrix = []

        grid = QGridLayout()
        self.setLayout(grid)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 1, 9, 9)
        print(self.listWidget.selectedItems())
        self.executeBtn.clicked.connect(self.handler_execute_from_listbox)
        self.loadBtn.clicked.connect(self.handler_load_from_file)
        self.generateBtn.clicked.connect(self.handler_generate_graph)

    def handler_load_from_file(self):
        self.set_file_mod()
        self.matrix = self.get_matrix()

    def handler_generate_next(self):
        self.set_generation_mod()
        self.matrix = self.get_matrix()
        stat = get_matrix_stats(self.matrix)
        self.label_vertexes.setText('Vertexes: ' + str(stat['v']))
        self.label_edges.setText('Edges: ' + str(stat['e']))

    def handler_generate_graph(self):
        self.set_generation_mod()

    def set_file_mod(self):
        self.GENERATE = False

    def set_generation_mod(self):
        self.GENERATE = True

    def handler_execute_from_listbox(self):
        commands = []
        for item in self.listWidget.selectedItems():
            commands.append(item.text())
        for command in commands:
            self.HANDLER_DICT[command]()

    def __get_gen_atributes(self):
        try:
            x, y = int(self.editVertex.text()), int(self.editEdges.text())
        except:
            x, y = 7, 10
        return x, y

    def get_matrix(self):
        if self.GENERATE:
            n, m = self.__get_gen_atributes()
            M = generator.GraphGenerator(n, m)
            M = next(M)
        else:
            M = Graph.readMatrixFromFile(self.lineEdit.text())
        return M

    def handler_push_flow(self):
        M = self.matrix
        G = Graph.initGraphFromMatrix(M)
        s, t = 0, len(M) - 1
        self.flow_algorithm = PushFlow(G, len(M), s, t)
        self.label_time.setText("Time: {:.6f} sec".format(self.flow_algorithm.time))
        self.label_flow.setText("Flow: {}".format(self.flow_algorithm.getMaxFlow()))
        self.__draw(G)

    def handler_dinica(self):
        M = self.matrix
        G = Graph.initGraphFromMatrix(M)
        s, t = 0, len(M) - 1
        self.flow_algorithm = Dinica(G, len(M), s, t)
        self.label_time.setText("Time: {:.6f} sec".format(self.flow_algorithm.time))
        self.label_flow.setText("Flow: {}".format(self.flow_algorithm.getMaxFlow()))
        self.__draw(G)

    def __draw(self, G):
        self.figure.clf()
        gv = GraphViz(G)
        plt.axis('off')
        gv.draw()
        self.canvas.draw_idle()


def main():
    clear_log()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
