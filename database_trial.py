# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 21:51:11 2019

@author: DELL
"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QVBoxLayout,QLineEdit,QScrollArea,QScroller,QGridLayout,QFormLayout, QWidget, QPushButton,QSizePolicy
from PyQt5.QtGui import QFont


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import Direct as dc
import FileConversion as fc
import multi as mt
#import Multithreading as opt

class showIdatabase(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Initial Database")
        self.setGeometry(100,100,600,600)
        self.main_widget = QWidget(self)
        #l = QVBoxLayout(self.main_widget)
        final_csv=open("Database10k.csv","r")##
        #grid=QGridLayout(self.main_widget)
        scroll_area = QScrollArea(self.main_widget)
        
        #l.addWidget(scroll_area)
        #l.setSpacing(15)
        scroll_widget =QWidget()
        scroll_layout = QFormLayout(scroll_widget)
        i=5
        for line in final_csv:
            self.label=QLabel(self.main_widget)
            #arr=line.split(",")
            #l1=" ".join(arr)
            self.label.setText(repr(line))
            self.label.setFont(QFont("Times", 12))
            #l.addWidget(self.label)
            #self.label.move(120,60+i)
            scroll_layout.addRow(self.label)
            #self.label.move(10,i)
            i=i+15
    
    
        scroll_area.setWidget(scroll_widget)
        #QScroller.grabGesture(
        #        scroll_area.viewport(), QScroller.LeftMouseButtonGesture
        #        )
        '''
        self.label=QLabel(self.main_widget)
        self.label.setText("robin")
        self.label.setFont(QFont("Times", 12, QFont.Bold))
        self.label.move(120,i)
        #l.addWidget(self.label)
        self.button = QPushButton('Close')
        self.button.clicked.connect(self.close)
        self.button.move(120,i+15,)
        #l.addWidget(self.button)
        '''
     
class DCWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("DC Graph")
        self.setGeometry(100,100,600,600)
        
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        
        obj=dc_plot(self.main_widget, width=5, height=4, dpi=100)
        
        #self.button = QPushButton('Switch Window')
        #self.button.clicked.connect(self.switch)
        l.addWidget(obj)
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        l.addWidget(self.button)

class AllWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("DC Graph")
        self.setGeometry(100,100,1000,1000)
        
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        
        obj=all_plot(self.main_widget, width=10, height=8, dpi=70)
        
        #self.button = QPushButton('Switch Window')
        #self.button.clicked.connect(self.switch)
        l.addWidget(obj)
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        l.addWidget(self.button)

    
class FCWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("FC Graph")
        self.setGeometry(100,100,600,600)
        
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        
        obj=fc_plot(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(obj)
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)
        l.addWidget(self.button)

class OPTWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Optimum records Graph")
        self.setGeometry(100,100,600,600)
        
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        
        obj=opt_plot(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(obj)
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)
        l.addWidget(self.button)
        
class MTWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Mutithreading Graph")
        self.setGeometry(100,100,600,600)
        
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        
        obj=mt_plot(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(obj)
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)
        l.addWidget(self.button)
        
class MyAllCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=10, height=8, dpi=70):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(221)
        self.axes2=fig.add_subplot(222)
        self.axes3=fig.add_subplot(223)
        self.axes4=fig.add_subplot(224)
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)
        self.plot()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        pass
  
class all_plot( MyAllCanvas):
    def plot(self):
        x=[10,20,30,40,50,60,70,80,90,100]
        y1=time_dc
        y2=time_fc
        y3=time_opt
        y4=time_mt
        #ax = self.figure.add_subplot(111)
        self.axes1.plot(x,y1)
        self.axes2.plot(x,y2)
        self.axes3.plot(x,y3)
        self.axes4.plot(x,y4)
        self.axes1.set_title('DC Graph')
        self.axes2.set_title('FC Graph')
        self.axes3.set_title('optimum files multithreading')
        self.axes4.set_title('Mutithreading graph')

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)
        self.plot()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        pass
  
class dc_plot( MyMplCanvas):
    def plot(self):
        y=[]
        y=time_dc
        x=[10,20,30,40,50,60,70,80,90,100]
        #ax = self.figure.add_subplot(111)
        self.axes.plot(x,y)
        self.axes.set_title('DC Graph')
        

class fc_plot( MyMplCanvas):
    def plot(self):
        y=[]
        y=time_fc
        x=[10,20,30,40,50,60,70,80,90,100]
        #ax = self.figure.add_subplot(111)
        self.axes.plot(x,y)
        self.axes.set_title('FC Graph')
        #self.draw()

class opt_plot( MyMplCanvas):
    def plot(self):
        y=[]
        y=time_opt
        x=[10,20,30,40,50,60,70,80,90,100]
        #ax = self.figure.add_subplot(111)
        self.axes.plot(x,y)
        self.axes.set_title('Optimum Records for Threading Graph')
        #self.draw()
        
class mt_plot( MyMplCanvas):
    def plot(self):
        y=[]
        y=time_mt
        x=[10,20,30,40,50,60,70,80,90,100]
        #ax = self.figure.add_subplot(111)
        self.axes.plot(x,y)
        self.axes.set_title('Multithreading Graph')
        #self.draw()


class Login(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('ETL Database')
        self.setGeometry(100, 100, 600, 600)
        self.main_widget = QWidget(self)
        #grid = QGridLayout()
        #grid.setSpacing(20)
        '''
        self.labelA=QLabel(self.main_widget)
        self.labelA.setText("Show Initial Database:")
        self.labelA.setFont(QFont("Times", 12, QFont.Bold))
        self.buttonA = QPushButton('Click me',self.main_widget)
        self.buttonA.clicked.connect(self.switch_data)
        self.labelA.move(50,100)
        #self.button.resize()
        self.buttonA.move(350,100)
        '''

        
        self.labelA=QLabel(self.main_widget)
        self.labelA.setText("Show Direct Conversion time graph:")
        self.labelA.setFont(QFont("Times", 12, QFont.Bold))
        self.buttonA = QPushButton('Click me',self.main_widget)
        self.buttonA.clicked.connect(self.direct)
        self.labelA.move(50,100)
        self.buttonA.move(390,100)
        
        self.labelB=QLabel(self.main_widget)
        self.labelB.setText("Show File Conversion time graph:")
        self.labelB.setFont(QFont("Times", 12, QFont.Bold))
        self.buttonB = QPushButton('Click me',self.main_widget)
        self.buttonB.clicked.connect(self.fileConv)
        self.labelB.move(50,130)
        self.buttonB.move(390,130)
        
        self.labelC=QLabel(self.main_widget)
        self.labelC.setText("Show optimum fils for multithreading:")
        self.labelC.setFont(QFont("Times", 12, QFont.Bold))
        self.buttonC = QPushButton('Click me',self.main_widget)
        self.buttonC.clicked.connect(self.opti)
        self.labelC.move(50,160)
        self.buttonC.move(390,160)
        
        self.labelD=QLabel(self.main_widget)
        self.labelD.setText("Show Multithreading Conversion time graph:")
        self.labelD.setFont(QFont("Times", 12, QFont.Bold))
        self.buttonD = QPushButton('Click me',self.main_widget)
        self.buttonD.clicked.connect(self.multi)
        self.labelD.move(50,190)
        self.buttonD.move(390,190)
        
        self.label=QLabel(self.main_widget)
        self.label.setText("Show All graph:")
        self.label.setFont(QFont("Times", 12, QFont.Bold))
        self.button = QPushButton('Click me',self.main_widget)
        self.button.clicked.connect(self.allgraph)
        self.label.move(50,220)
        self.button.move(370,220)
        
        
    
    def switch_data(self):
         self.window=showIdatabase()
         self.window.show()
         
    def direct(self):
        self.window = DCWindow()
        self.window.show()
        
    
    def fileConv(self):
        self.window = FCWindow()
        self.window.show()
        
    def opti(self):
        self.window = OPTWindow()
        self.window.show()
        
    def multi(self):
        self.window = MTWindow()
        self.window.show()
    
    def allgraph(self):
        self.window = AllWindow()
        self.window.show()
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    login=Login()
    login.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    time_dc=[]
    time_dc=dc.main()
    time_fc=[]
    time_fc=fc.main()
    time_opt=[]
    time_mt=[]
    time_opt,time_mt=mt.main()
    main()
    
    
    
