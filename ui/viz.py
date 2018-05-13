# coding=utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import generator
from graph import Graph
from algorithms.pushFlow import PushFlow
from algorithms.dinica import Dinica
from ui import design
from ui.graphViz import GraphViz
from utils import log_report, clear_log, get_matrix_stats, generator_read_file
import matplotlib.pyplot as plt


class ExampleApp(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.GENERATE = True
        self.HANDLER_DICT = {"Алгоритм Диницы": self.handler_dinica,
                             "Проталкивание предпотока": self.handler_push_flow,
                             "Режим генерации": self.handler_generate_graph,
                             "Режим считывания из файла": self.handler_load_from_file,
                             "Создать новый граф": self.handler_generate_next,
                             "Отрисовать всё": self.handler_draw_graph,
                             "Отрисовать только путь": self.handler_draw_onlyway_graph,
                             "Провести эксперимент": self.handler_experiment}
        self.flow_algorithm = None
        self.graph = None
        self.matrix = []

        grid = QGridLayout()
        self.setLayout(grid)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 1, 9, 9)
        print(self.listWidget.selectedItems())
        self.executeBtn.clicked.connect(self.handler_execute_from_listbox)
        self.loadBtn.clicked.connect(self.handler_load_from_file)
        self.listWidget.itemDoubleClicked.connect(self.handler_double_clicked_list)

    def handler_draw_graph(self):
        self.__draw(self.flow_algorithm.getGraph())

    def handler_draw_onlyway_graph(self):
        self.__draw(self.flow_algorithm.getGraph(), True)

    def handler_load_from_file(self):
        self.set_file_mod()
        self.matrix = self.get_matrix()

    def handler_generate_next(self):
        self.set_generation_mod()
        self.matrix = self.get_matrix()
        stat = get_matrix_stats(self.matrix)
        self.label_vertexes.setText('Кол-во вершин: ' + str(stat['v']))
        self.label_edges.setText('Кол-во ребер: ' + str(stat['e']))
        self.set_status('создан новый граф')

    def handler_experiment(self):
        count = int(self.editExperimentCount.text())

        if self.GENERATE:
            n, m = self.__get_gen_atributes()
            gen = generator.GraphGenerator(n, m)
        else:
            gen = generator_read_file

        ans_dinica = 0
        ans_preflow = 0

        for idx in range(count):
            M = next(gen)
            s, t = 0, len(M) - 1

            graph = Graph.initGraphFromMatrix(M)
            dinica_algorithm = Dinica(graph, len(M), s, t)

            graph = Graph.initGraphFromMatrix(M)
            preflow_algorithm = PushFlow(graph, len(M), s, t)

            ans_dinica += dinica_algorithm.time
            ans_preflow += preflow_algorithm.time
        self.set_status('{} тестов, Диница: {}, проталкивание предпотока: {}'.format(count, ans_dinica, ans_preflow))





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

    def handler_double_clicked_list(self, item):
        self.HANDLER_DICT[item.text()]()

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
        self.graph = Graph.initGraphFromMatrix(M)
        s, t = 0, len(M) - 1
        self.flow_algorithm = PushFlow(self.graph, len(M), s, t)
        self.label_time.setText("Время: {:.6f} sec".format(self.flow_algorithm.time))
        self.label_flow.setText("Максимальный поток: {}".format(self.flow_algorithm.getMaxFlow()))
        self.set_status('выполнен алгоритм проталкивания предпотока')

    def handler_dinica(self):
        M = self.matrix
        self.graph = Graph.initGraphFromMatrix(M)
        s, t = 0, len(M) - 1
        self.flow_algorithm = Dinica(self.graph, len(M), s, t)
        self.label_time.setText("Время: {:.6f} sec".format(self.flow_algorithm.time))
        self.label_flow.setText("Максимальный поток: {}".format(self.flow_algorithm.getMaxFlow()))
        self.set_status('выполнен алгоритм Диницы')

    def set_status(self, text):
        if self.GENERATE:
            mod = 'генерация случаного графа'
        else:
            mod = 'чтение из файла'

        self.label_status.setText('Последнее действие: {}, Режим работы: {}'.format(text, mod))

    def __draw(self, G, only_way=False):
        self.figure.clf()
        gv = GraphViz(G, only_way)
        plt.axis('off')
        gv.draw()
        self.canvas.draw_idle()


def run():
    clear_log()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    run()
