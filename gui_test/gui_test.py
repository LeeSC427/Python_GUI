import sys
from PyQt5.QtWidgets import *
import pyqtgraph

class point:
    def __init__(self, x, y):
        self.x = [x]
        self.y = [y]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.x = [1]
        self.y = [1]

        self.point_1 = point(2, 13)
        self.point_2 = point(4, 5)
        self.point_3 = point(8, 11)
        #self.point_array = [self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, self.point_3.x, self.point_3.y]
        self.point_array = [2,13,4,5,8,11]

        self.graphWidget = pyqtgraph.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.button_all = QPushButton("ALL",self)
        self.button_1 = QPushButton("point_1",self)
        self.button_2 = QPushButton("point_2",self)
        self.button_3 = QPushButton("point_3",self)

        self.button_all.move(20,10)
        self.button_1.move(170,10)
        self.button_2.move(320,10)
        self.button_3.move(470,10)

        self.button_all.setEnabled(True)
        self.button_1.setEnabled(True)
        self.button_2.setEnabled(True)
        self.button_3.setEnabled(True)

        self.pen = pyqtgraph.mkPen(color=(0,0,0))
        self.data_1 = self.graphWidget.plot(self.x, self.y, name="point", pen=self.pen, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
        #self.button_all.clicked.connect(lambda: self.plot_all(self.point_array))
        #self.button_all.clicked.connect(lambda x_1=self.point_1.x, y_1=self.point_1.y, x_2=self.point_2.x, y_2=self.point_2.y, x_3=self.point_3.x, y_3=self.point_3.y: self.plot_all(x_1, y_1, x_2, y_2, x_3, y_3))
        self.button_all.clicked.connect(lambda: self.plot(self.point_1.x, self.point_1.y))
        #self.button_all.clicked.connect(lambda: self.plot(self.point_2.x, self.point_2.y))
        #self.button_all.clicked.connect(lambda: self.plot(self.point_3.x, self.point_3.y))

        self.graphWidget.setBackground('w')
        self.graphWidget.setXRange(-300/100,4000/100, padding = 0)
        self.graphWidget.setYRange(-300/100,4000/100, padding = 0)
        self.graphWidget.setLabel("left", "Y-axis[m]")
        self.graphWidget.setLabel("bottom", "X-axis[m]")
        self.graphWidget.addLegend()

        self.graphWidget.showGrid(x=True, y=True)

    #def plot_all(self, array):
    #    pen_1 = pyqtgraph.mkPen(color=(0,0,0))
    #    pen_2 = pyqtgraph.mkPen(color=(255,255,255))
    #    pen_3 = pyqtgraph.mkPen(color=(127,127,127))
    #    self.graphWidget.plot(array[0], array[1], name="point_1", pen=pen_1, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
    #    self.graphWidget.plot(array[2], array[3], name="point_2", pen=pen_2, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
    #    self.graphWidget.plot(array[4], array[5], name="point_3", pen=pen_3, symbol='o', symbolSize=10, symbolBrush=((0,0,0)))
        
    def plot(self, x, y):
        pen = pyqtgraph.mkPen(color=(0,0,0))
        self.data_1.setData(x,y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
