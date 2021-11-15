import sys
import numpy

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.Qt import *

class PlotWidget(QWidget):
    def __init__(self):
        super(PlotWidget, self).__init__()
        self.mainLayout = QVBoxLayout(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.mainLayout.addWidget(self.canvas)

    def func(data):
        return numpy.abs(numpy.cos(2*data))/numpy.cos(data)

    def plot(self):
        x = numpy.linspace(-10, 10, 1000)
        y = PlotWidget.func(x)

        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDFFF')
        
        ax.axhline(y=0, xmin= -10, xmax=10, color='#000000')
        ax.axvline(x=0, ymin= -5, ymax=5, color='#000000')        

        ax.set_ylim([-4, 4])
        ax.set_xlim([-8, 8])
                   
        ax.plot(x, y, color='#0000FF')
        self.canvas.draw()    

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()
        self.connectUi()

    def initUi(self):
        self.centralWidget = QWidget(self)

        self.l = QVBoxLayout(self.centralWidget)
        self.bl = QHBoxLayout(self.centralWidget)

        self.plotWidget = PlotWidget()

        self.plotButton = QPushButton('Построить график')
        self.clearButton = QPushButton('Очистить поле')
        self.plotButton.setStyleSheet('font-size: 12pt; font-weight: 36;')
        self.clearButton.setStyleSheet('font-size: 12pt; font-weight: 36;')

        self.bl.addWidget(self.plotButton)
        self.bl.addWidget(self.clearButton)

        self.l.addLayout(self.bl)
        self.l.addWidget(self.plotWidget)

        self.setCentralWidget(self.centralWidget)

    def connectUi(self):
        self.plotButton.clicked.connect(self.plotWidget.plot)
        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        self.plotWidget.figure.clear()
        self.plotWidget.canvas.draw()        

app = QApplication([])
p = MainWindow()
p.show()

sys.exit(app.exec_())