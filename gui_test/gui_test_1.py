import sys 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import pyqtgraph
import random
from time import time

class point:
    def __init__(self, x, y): 
        self.x = [x] 
        self.y = [y] 
        self.time = 0.0

    def update_point(self):
        t1 = time()
        
        if t1 - self.time > 0.5:
            self.x[0] = random.uniform(-0.3,3)
            self.y[0] = random.uniform(-0.3,3)
            self.time = time()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.first_run = True
        self.button_pushed = [False, False, False]

        self.point_1 = point(1, 2)
        self.point_2 = point(1, 2)
        self.point_3 = point(1, 2)

        self.x = [1]
        self.y = [2]

        self.graphWidget = pyqtgraph.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.setFixedWidth(1000)
        self.setFixedHeight(1000)
        self.pen = pyqtgraph.mkPen(color=(0,0,0))

        self.button_all = QPushButton("ALL",self)
        self.button_1 = QPushButton("point_1",self)
        self.button_2 = QPushButton("point_2",self)
        self.button_3 = QPushButton("point_3",self)

        self.set_button()
        
        self.data_1 = self.graphWidget.plot(self.point_1.x, self.point_1.y, name="point_1", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
        self.data_2 = self.graphWidget.plot(self.point_2.x, self.point_2.y, name="point_2", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((255,255,0)))
        self.data_3 = self.graphWidget.plot(self.point_3.x, self.point_3.y, name="point_3", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((255,0,255)))

        #self.data_1 = self.subplot.plot(self.point_1.x, self.point_1.y, name="point_1", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
        #self.data_2 = self.subplot.plot(self.point_2.x, self.point_2.y, name="point_2", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((255,255,0)))
        #self.data_3 = self.subplot.plot(self.point_3.x, self.point_3.y, name="point_3", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((255,0,255)))

        self.graphWidget.setBackground('w')
        self.graphWidget.setXRange(-300/1000,4000/1000, padding = 0)
        self.graphWidget.setYRange(-300/1000,4000/1000, padding = 0)
        self.graphWidget.setLabel("left", "Y-axis[m]")
        self.graphWidget.setLabel("bottom", "X-axis[m]")
        self.graphWidget.addLegend()

        self.graphWidget.showGrid(x=True, y=True)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.run)
        self.timer.start()

        self.run()

    def set_button(self):

        self.button_all.move(20,10)
        self.button_1.move(170,10)
        self.button_2.move(320,10)
        self.button_3.move(470,10)

        self.button_all.setEnabled(True)
        self.button_1.setEnabled(True)
        self.button_2.setEnabled(True)
        self.button_3.setEnabled(True)

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

    def plot(self, data, x, y):
        pen = pyqtgraph.mkPen(color=(0,0,0))
        data.setData(x,y)

    def run(self):
        self.point_1.update_point()
        self.point_2.update_point()
        self.point_3.update_point()
        print(self.button_pushed)
        
        if self.button_pushed[0] & self.button_pushed[1] & self.button_pushed[2]:
            self.data_1.setData(self.point_1.x, self.point_1.y)
            self.data_2.setData(self.point_2.x, self.point_2.y)
            self.data_3.setData(self.point_3.x, self.point_3.y)
            self.data_1.show()
            self.data_2.show()
            self.data_3.show()
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

