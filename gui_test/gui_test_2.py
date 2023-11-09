import sys 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter,QPen, QColor, QBrush
import pyqtgraph
import random
import matplotlib.pyplot as plt
from time import time
import numpy as np

class point:
    def __init__(self, x, y):
        self.x = [x]
        self.y = [y]
        self.time = 0.0

    def update_point(self):
        #t1 = time()

        #if t1 - self.time > 0.5:
        #    self.x[0] = random.uniform(30,730)
        #    self.y[0] = random.uniform(120,450)
        #    self.time = time()

        self.x[0] = random.uniform(30,730)
        self.y[0] = random.uniform(120,450)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.button_pushed = [False, False, False]

        self.graphWidget = pyqtgraph.PlotWidget()
        #self.setCentralWidget(self.graphWidget)

        self.point_1 = point(380,285)
        self.point_2 = point(380,285)
        self.point_3 = point(380,285)

        self.button_all = QPushButton("ALL", self)
        self.button_1 = QPushButton("point_1", self)
        self.button_2 = QPushButton("point_2", self)
        self.button_3 = QPushButton("point_3", self)

        self.pen = pyqtgraph.mkPen(color=(0,0,0))

        self.data_1 = self.graphWidget.plot(self.point_1.x, self.point_1.y, name="point_1", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
        self.data_2 = self.graphWidget.plot(self.point_2.x, self.point_2.y, name="point_2", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((255,255,0)))
        self.data_3 = self.graphWidget.plot(self.point_3.x, self.point_3.y, name="point_3", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((255,0,255)))

        self.initUI()
        self.setButton()
        self.timer_event()

    def initUI(self):
        self.setGeometry(300,300,1000,600)
        self.setWindowTitle("test")

    def setButton(self):
        self.button_all.move(20,20)
        self.button_1.move(270,20)
        self.button_2.move(520,20)
        self.button_3.move(770,20)

        self.button_all.resize(200,60)
        self.button_1.resize(200,60)
        self.button_2.resize(200,60)
        self.button_3.resize(200,60)

        self.button_all.clicked.connect(self.button_func_all)
        self.button_1.clicked.connect(self.button_func_1)
        self.button_2.clicked.connect(self.button_func_2)
        self.button_3.clicked.connect(self.button_func_3)

    def button_func_all(self):
        self.button_pushed = [True, True, True]
    def button_func_1(self):
        self.button_pushed = [True, False, False]
    def button_func_2(self):
        self.button_pushed = [False, True, False]
    def button_func_3(self):
        self.button_pushed = [False, False, True]

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(255,255,255)) #set background color
        qp.setPen(QPen(QColor(0,0,200), 3))
        qp.drawRect(30,600-450-30,730,450)

    def timer_event(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def run(self):
        self.point_1.update_point()
        self.point_2.update_point()
        self.point_3.update_point()

        if False not in self.button_pushed:
            self.data_1.setData(self.point_1.x, self.point_1.y)
            self.data_2.setData(self.point_2.x, self.point_2.y)
            self.data_3.setData(self.point_3.x, self.point_3.y)
        elif self.button_pushed[0] is True:
            self.data_1.setData(self.point_1.x, self.point_1.y)
            self.data_1.show()
            self.data_2.hide()
            self.data_3.hide()
        elif self.button_pushed[1] is True:
            self.data_1.hide()
            self.data_2.setData(self.point_2.x, self.point_2.y)
            self.data_2.show()
            self.data_3.hide()
        elif self.button_pushed[2] is True:
            self.data_1.hide()
            self.data_2.hide()
            self.data_3.setData(self.point_3.x, self.point_3.y)
            self.data_3.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
