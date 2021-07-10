import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets , QtPrintSupport
import pandas as pd
from pyqtgraph import PlotWidget ,PlotItem
import pyqtgraph as pg 
import os 
import pathlib
import matplotlib.pyplot as plt
from scipy import signal
from fpdf import FPDF
import shutil
from datetime import datetime
import pyqtgraph.exporters

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 939)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(11, 60, 1214, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 20, 1171, 768))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.r1 = QtWidgets.QRadioButton(self.widget)
        self.r1.setText("")
        self.r1.setObjectName("r1")
        self.r1.value=1
        self.verticalLayout.addWidget(self.r1)
        self.label_Channel1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Channel1.setFont(font)
        self.label_Channel1.setObjectName("label_Channel1")
        self.verticalLayout.addWidget(self.label_Channel1)
        self.Channel_1 = PlotWidget(self.widget)
        self.Channel_1.setObjectName("Channel_1")
        self.verticalLayout.addWidget(self.Channel_1)
        self.r2 = QtWidgets.QRadioButton(self.widget)
        self.r2.setText("")
        self.r2.setObjectName("r2")
        self.r2.value=2
        self.verticalLayout.addWidget(self.r2)
        self.label_Channel2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Channel2.setFont(font)
        self.label_Channel2.setObjectName("label_Channel2")
        self.verticalLayout.addWidget(self.label_Channel2)
        self.Channel_2 = PlotWidget(self.widget)
        self.Channel_2.setObjectName("Channel_2")
        self.verticalLayout.addWidget(self.Channel_2)
        self.r3 = QtWidgets.QRadioButton(self.widget)
        self.r3.setText("")
        self.r3.setObjectName("r3")
        self.r3.value=3
        self.verticalLayout.addWidget(self.r3)
        self.label_Channel3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Channel3.setFont(font)
        self.label_Channel3.setObjectName("label_Channel3")
        self.verticalLayout.addWidget(self.label_Channel3)
        self.Channel_3 = PlotWidget(self.widget)
        self.Channel_3.setObjectName("Channel_3")
        self.verticalLayout.addWidget(self.Channel_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_Spectrogram_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Spectrogram_1.setFont(font)
        self.label_Spectrogram_1.setObjectName("label_Spectrogram_1")
        self.verticalLayout_2.addWidget(self.label_Spectrogram_1)
        self.Spectrogram_1 = pg.GraphicsLayoutWidget(self.widget)
        self.Spectrogram_1.setObjectName("Spectrogram_1")
        self.verticalLayout_2.addWidget(self.Spectrogram_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_Spectrogram_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Spectrogram_2.setFont(font)
        self.label_Spectrogram_2.setObjectName("label_Spectrogram_2")
        self.verticalLayout_2.addWidget(self.label_Spectrogram_2)
        self.Spectrogram_2 = pg.GraphicsLayoutWidget(self.widget)
        self.Spectrogram_2.setObjectName("Spectrogram_2")
        self.verticalLayout_2.addWidget(self.Spectrogram_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_Spectrogram_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Spectrogram_3.setFont(font)
        self.label_Spectrogram_3.setObjectName("label_Spectrogram_3")
        self.verticalLayout_2.addWidget(self.label_Spectrogram_3)
        self.Spectrogram_3 = pg.GraphicsLayoutWidget(self.widget)
        self.Spectrogram_3.setObjectName("Spectrogram_3")
        self.verticalLayout_2.addWidget(self.Spectrogram_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 10, 461, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExitButton = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitButton.sizePolicy().hasHeightForWidth())
        self.ExitButton.setSizePolicy(sizePolicy)
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ExitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon)
        self.ExitButton.setIconSize(QtCore.QSize(25, 25))
        self.ExitButton.setFlat(True)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.play = QtWidgets.QPushButton(self.widget1)
        self.play.setAutoFillBackground(False)
        self.play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setIconSize(QtCore.QSize(25, 25))
        self.play.setDefault(False)
        self.play.setFlat(True)
        self.play.setObjectName("images/play")
        self.horizontalLayout.addWidget(self.play)
        self.pause = QtWidgets.QPushButton(self.widget1)
        self.pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon2)
        self.pause.setIconSize(QtCore.QSize(25, 25))
        self.pause.setFlat(True)
        self.pause.setObjectName("pause")
        self.horizontalLayout.addWidget(self.pause)
        self.speed_down = QtWidgets.QPushButton(self.widget1)
        self.speed_down.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Decreese_Speed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speed_down.setIcon(icon3)
        self.speed_down.setIconSize(QtCore.QSize(25, 25))
        self.speed_down.setFlat(True)
        self.speed_down.setObjectName("speed_down")
        self.horizontalLayout.addWidget(self.speed_down)
        self.speed_up = QtWidgets.QPushButton(self.widget1)
        self.speed_up.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Increase_Speed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speed_up.setIcon(icon4)
        self.speed_up.setIconSize(QtCore.QSize(25, 25))
        self.speed_up.setFlat(True)
        self.speed_up.setObjectName("speed_up")
        self.horizontalLayout.addWidget(self.speed_up)
        self.zoom_in = QtWidgets.QPushButton(self.widget1)
        self.zoom_in.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/zoomin.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in.setIcon(icon5)
        self.zoom_in.setIconSize(QtCore.QSize(30, 30))
        self.zoom_in.setFlat(True)
        self.zoom_in.setObjectName("zoom_in")
        self.horizontalLayout.addWidget(self.zoom_in)
        self.zoom_out = QtWidgets.QPushButton(self.widget1)
        self.zoom_out.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/zoom out.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon6)
        self.zoom_out.setIconSize(QtCore.QSize(30, 30))
        self.zoom_out.setFlat(True)
        self.zoom_out.setObjectName("zoom_out")
        self.horizontalLayout.addWidget(self.zoom_out)
        self.zoomx = QtWidgets.QPushButton(self.widget1)
        self.zoomx.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/zoom x.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomx.setIcon(icon7)
        self.zoomx.setIconSize(QtCore.QSize(100, 100))
        self.zoomx.setFlat(True)
        self.zoomx.setObjectName("zoomx")
        self.horizontalLayout.addWidget(self.zoomx)
        self.zoomy = QtWidgets.QPushButton(self.widget1)
        self.zoomy.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/zoom y.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomy.setIcon(icon8)
        self.zoomy.setIconSize(QtCore.QSize(50, 50))
        self.zoomy.setFlat(True)
        self.zoomy.setObjectName("zoomy")
        self.horizontalLayout.addWidget(self.zoomy)
        self.clear_Button = QtWidgets.QPushButton(self.widget1)
        self.clear_Button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/delete-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_Button.setIcon(icon9)
        self.clear_Button.setIconSize(QtCore.QSize(25, 25))
        self.clear_Button.setFlat(True)
        self.clear_Button.setObjectName("clear_Button")
        self.horizontalLayout.addWidget(self.clear_Button)
        self.Export = QtWidgets.QPushButton(self.widget1)
        self.Export.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/pdf-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Export.setIcon(icon10)
        self.Export.setIconSize(QtCore.QSize(25, 25))
        self.Export.setFlat(True)
        self.Export.setObjectName("Export")
        self.horizontalLayout.addWidget(self.Export)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(490, 20, 177, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scroll_x = QtWidgets.QSlider(self.widget2)
        self.scroll_x.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_x.setObjectName("scroll_x")
        self.horizontalLayout_2.addWidget(self.scroll_x)
        self.scroll_y = QtWidgets.QSlider(self.widget2)
        self.scroll_y.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_y.setObjectName("scroll_y")
        self.horizontalLayout_2.addWidget(self.scroll_y)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuGenerate = QtWidgets.QMenu(self.menubar)
        self.menuGenerate.setObjectName("menuGenerate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Play_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Play_Signal_1.setObjectName("Play_Signal_1")
        self.Pause_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Pause_Signal_1.setObjectName("Pause_Signal_1")
        self.Clear_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Clear_Signal_1.setObjectName("Clear_Signal_1")
        self.Play_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Play_Signal_2.setObjectName("Play_Signal_2")
        self.Pause_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Pause_Signal_2.setObjectName("Pause_Signal_2")
        self.Clear_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Clear_Signal_2.setObjectName("Clear_Signal_2")
        self.Play_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Play_Signal_3.setObjectName("Play_Signal_3")
        self.Pause_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Pause_Signal_3.setObjectName("Pause_Signal_3")
        self.Clear_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Clear_Signal_3.setObjectName("Clear_Signal_3")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionOpen_3 = QtWidgets.QAction(MainWindow)
        self.actionOpen_3.setObjectName("actionOpen_3")
        self.OpenChannel_1 = QtWidgets.QAction(MainWindow)
        self.OpenChannel_1.setObjectName("OpenChannel_1")
        self.OpenChannel_2 = QtWidgets.QAction(MainWindow)
        self.OpenChannel_2.setObjectName("OpenChannel_2")
        self.OpenChannel_3 = QtWidgets.QAction(MainWindow)
        self.OpenChannel_3.setObjectName("OpenChannel_3")
        self.zoom_x_Signal_1 = QtWidgets.QAction(MainWindow)
        self.zoom_x_Signal_1.setObjectName("zoom_x_Signal_1")
        self.zoom_x_Signal_2 = QtWidgets.QAction(MainWindow)
        self.zoom_x_Signal_2.setObjectName("zoom_x_Signal_2")
        self.zoom_x_Signal_3 = QtWidgets.QAction(MainWindow)
        self.zoom_x_Signal_3.setObjectName("zoom_x_Signal_3")
        self.zoom_y_Signal_1 = QtWidgets.QAction(MainWindow)
        self.zoom_y_Signal_1.setObjectName("zoom_y_Signal_1")
        self.zoom_y_Signal_2 = QtWidgets.QAction(MainWindow)
        self.zoom_y_Signal_2.setObjectName("zoom_y_Signal_2")
        self.zoom_y_Signal_3 = QtWidgets.QAction(MainWindow)
        self.zoom_y_Signal_3.setObjectName("zoom_y_Signal_3")
        self.Export_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Export_Signal_1.setObjectName("Export_Signal_1")
        self.Export_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Export_Signal_2.setObjectName("Export_Signal_2")
        self.Export_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Export_Signal_3.setObjectName("Export_Signal_3")
        self.Signal_1_Spectrogram = QtWidgets.QAction(MainWindow)
        self.Signal_1_Spectrogram.setObjectName("Signal_1_Spectrogram")
        self.Signal_2_Spectrogram = QtWidgets.QAction(MainWindow)
        self.Signal_2_Spectrogram.setObjectName("Signal_2_Spectrogram")
        self.Signal_3_Spectrogram = QtWidgets.QAction(MainWindow)
        self.Signal_3_Spectrogram.setObjectName("Signal_3_Spectrogram")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_X = QtWidgets.QAction(MainWindow)
        self.actionZoom_X.setObjectName("actionZoom_X")
        self.actionZoom_Y = QtWidgets.QAction(MainWindow)
        self.actionZoom_Y.setObjectName("actionZoom_Y")
        self.menuOpen.addAction(self.OpenChannel_1)
        self.menuOpen.addAction(self.OpenChannel_2)
        self.menuOpen.addAction(self.OpenChannel_3)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionZoom_X)
        self.menuView.addAction(self.actionZoom_Y)
        self.menuGenerate.addAction(self.Signal_1_Spectrogram)
        self.menuGenerate.addAction(self.Signal_2_Spectrogram)
        self.menuGenerate.addAction(self.Signal_3_Spectrogram)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGenerate.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.volt1=np.array([])
        self.volt2=np.array([])
        self.volt3=np.array([])

        self.speed1=10
        self.speed2=10
        self.speed3=10
        self.spectrogram1=0
        self.spectrogram2=0
        self.spectrogram3=0
        #Timers
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()

        

        #Triggers
        self.OpenChannel_1.triggered.connect(lambda : self.channel1_load())
        self.OpenChannel_2.triggered.connect(lambda : self.channel2_load())
        self.OpenChannel_3.triggered.connect(lambda: self.channel3_load())
        self.pause.clicked.connect(lambda : self.pause_fn() )
        self.play.clicked.connect(lambda :self.play_fn())
        self.zoomx.clicked.connect(lambda:self.zoom_x())
        self.zoomy.clicked.connect(lambda:self.zoom_y())
        self.speed_up.clicked.connect(lambda:self.speedup())
        self.speed_down.clicked.connect(lambda:self.speeddown())
        self.actionZoom_In.triggered.connect(lambda : self.zoom_i())
        self.actionZoom_Out.triggered.connect(lambda : self.zoom_o())
        self.actionZoom_X.triggered.connect(lambda:self.zoom_x())
        self.actionZoom_Y.triggered.connect(lambda:self.zoom_y())
        self.r1.toggled.connect(self.onclicked)
        self.r2.toggled.connect(self.onclicked)
        self.r3.toggled.connect(self.onclicked)
        self.Export.clicked.connect(lambda:self.printPDF())
        self.zoom_in.clicked.connect(lambda : self.zoom_i())
        self.zoom_out.clicked.connect(lambda : self.zoom_o())
        self.clear_Button.clicked.connect(lambda:self.clear())
        self.ExitButton.clicked.connect(exit)
        self.Signal_1_Spectrogram.triggered.connect(lambda:self.generate_spectrogram1())
        self.Signal_2_Spectrogram.triggered.connect(lambda:self.generate_spectrogram2())
        self.Signal_3_Spectrogram.triggered.connect(lambda:self.generate_spectrogram3())
        self.scroll_x.valueChanged.connect(self.scrollx)
        self.scroll_y.valueChanged.connect(self.scrolly)
        #Hidding
        self.Channel_1.hide()
        self.Channel_2.hide()
        self.Channel_3.hide()

        self.Spectrogram_1.hide()
        self.Spectrogram_2.hide()
        self.Spectrogram_3.hide()

        self.label_Channel1.hide()
        self.label_Channel2.hide()
        self.label_Channel3.hide()

        self.label_Spectrogram_1.hide()
        self.label_Spectrogram_2.hide()
        self.label_Spectrogram_3.hide()
        
        self.r1.hide()
        self.r2.hide()
        self.r3.hide()
        self.spec1=0
            

####################### Read Functions ################################
    def channel1_read(self) :
        self.fname1 = QtGui.QFileDialog.getOpenFileName( self, 'Open only CSV ', os.getenv('HOME') ,"csv(*.csv)" )
        path = self.fname1[0]
            
        if pathlib.Path(path).suffix == ".csv" :
            self.data1=pd.read_csv(path)
            self.time1=np.array(self.data1.iloc[:,0])
            self.volt1=np.array(self.data1.iloc[:,1])

        
    def channel2_read(self) :
        fname = QtGui.QFileDialog.getOpenFileName( self, 'Open only CSV ', os.getenv('HOME') ,"csv(*.csv)" )
        path = fname[0]
        if pathlib.Path(path).suffix == ".csv" :
            self.data2=pd.read_csv(path)
            self.time2=np.array(self.data2.iloc[:,0])
            self.volt2=np.array(self.data2.iloc[:,1])
       
    def channel3_read(self) :
        fname = QtGui.QFileDialog.getOpenFileName( self, 'Open only CSV', os.getenv('HOME') ,"csv(*.csv)" )
        path = fname[0]
        if pathlib.Path(path).suffix == ".csv" :
            self.data3=pd.read_csv(path)
            self.time3=np.array(self.data3.iloc[:,0])
            self.volt3=np.array(self.data3.iloc[:,1])
#######################################################################
####################### Load Functions ################################
    def channel1_load(self):  
        self.channel1_read()
        self.pen = pg.mkPen(color=(255, 255, 255),width=2)
        self.data_line1 =  self.Channel_1.plot( self.time1,self.volt1, pen=self.pen)
        self.Channel_1.plotItem.setLimits(xMin =0, xMax=1 , yMin =-1, yMax=1)
        
        self.idx1=0
        self.timer1.setInterval(100)

        self.timer1.timeout.connect(self.update_channel1)
        self.timer1.start()
        self.Channel_1.show()
        self.label_Channel1.show()
        self.r1.show()


    def channel2_load(self):

        self.channel2_read()
        self.pen = pg.mkPen(color=(0,160, 0),width=2)
        self.data_line2 = self.Channel_2.plot(self.time2, self.volt2, pen=self.pen)
        self.Channel_2.plotItem.setLimits(xMin =0, xMax=12 , yMin =-1, yMax=1)
        self.idx2 = 0
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(self.update_channel2)
        self.timer2.start()
        self.Channel_2.show()
        self.label_Channel2.show()
        self.r2.show()

    def channel3_load(self):

        self.channel3_read()
        self.pen = pg.mkPen(color=(255,255,0),width=2)
        self.data_line3 =  self.Channel_3.plot(self.time3, self.volt3, pen=self.pen)
        self.Channel_3.plotItem.setLimits(xMin =0, xMax=12, yMin =-1, yMax=1)
        
        self.idx3 = 0
        self.timer3.setInterval(100)
        self.timer3.timeout.connect(self.update_channel3)
        self.timer3.start()    
        self.Channel_3.show()
        self.label_Channel3.show()
        self.r3.show()
#######################################################################
####################### Update Functions ################################

    def update_channel1(self):
        t =  self.time1[:self.idx1]
        v = self.volt1[:self.idx1]  
        self.idx1 +=self.speed1
        if self.idx1 > len(self.time1) :
            self.idx1 = 0
        if  self.time1[self.idx1] >0.5:
            self.Channel_1.setLimits(xMin =min( t ,default=0 ) , xMax=max(t, default=0) ) 

        self.Channel_1.plotItem.setXRange(max(t,default=0)-0.5,max(t,default=0))
        self.data_line1.setData(t, v)  
        
     
    def update_channel2(self):
       
        t =  self.time2[:self.idx2]
        v = self.volt2[:self.idx2]  
        self.idx2 +=self.speed2
        if self.idx2 > len(self.time2) :
            self.idx2 = 0
        if  self.time2[self.idx2] >0.5:
            self.Channel_2.setLimits(xMin =min( t ,default=0 ) , xMax=max(t, default=0) ) 

        self.Channel_2.plotItem.setXRange(max(t,default=0)-0.5,max(t,default=0))
        self.data_line2.setData(t, v)  

    def update_channel3(self):

        t = self.time3[:self.idx3]
        v = self.volt3[:self.idx3]  
        self.idx3 +=self.speed3
        if self.idx3 > len(self.time3) :
            self.idx3 = 0
        if self.time3[self.idx3] > 0.5 :
            self.Channel_3.setLimits(xMin =min(t , default=0), xMax=max(t, default=0))

        self.Channel_3.plotItem.setXRange( max(t,default=0)-0.5 ,max(t,default=0)  )
        self.data_line3.setData(t, v)    
#######################################################################
   ##zoom in function
    def zoom_i (self):
        if self.c==1 :
            self.Channel_1.plotItem.getViewBox().scaleBy((0.75, 0.75))
            
        elif self.c==2  :
            self.Channel_2.plotItem.getViewBox().scaleBy((0.75, 0.75))
             
        elif self.c==3  :
            self.Channel_3.plotItem.getViewBox().scaleBy((0.75, 0.75))

    ##zoom out function
    def zoom_o (self):
        if self.c==1 :
            self.Channel_1.plotItem.getViewBox().scaleBy((1.25, 1.25))
            
        elif self.c==2  :
            self.Channel_2.plotItem.getViewBox().scaleBy((1.25,1.25))
             
        elif self.c==3  :
            self.Channel_3.plotItem.getViewBox().scaleBy((1.25,1.25))

    ## zoom x function
    def zoom_x (self):
        if self.c==1 :
            self.Channel_1.plotItem.getViewBox().scaleBy((0.75, 1))
            
        elif self.c==2  :
            self.Channel_2.plotItem.getViewBox().scaleBy((0.75,1))
             
        elif self.c==3  :
            self.Channel_3.plotItem.getViewBox().scaleBy((0.75,1))
    ## zoom y function

    def zoom_y (self):
        if self.c==1 :
            self.Channel_1.plotItem.getViewBox().scaleBy((1, 0.75))
            
        elif self.c==2  :
            self.Channel_2.plotItem.getViewBox().scaleBy((1,0.75))
             
        elif self.c==3  :
            self.Channel_3.plotItem.getViewBox().scaleBy((1,0.75))
    def speedup(self):
        if self.c==1 :
            if self.speed1 >= 10:
                self.speed1=self.speed1+10
            else:
                self.speed1=10  
        elif self.c==2  :
            if self.speed2 >= 10:
                self.speed2=self.speed2+10
            else:
                self.speed2=10 
   
        elif self.c==3  :
            if self.speed3 >= 10:
                self.speed3=self.speed3+10
            else:
                self.speed=10 
    def speeddown(self):
        if self.c==1 :
            if self.speed1 > 10:
                self.speed1=self.speed1-10
            else:
                self.speed1=10  
        elif self.c==2  :
            if self.speed2 > 10:
                self.speed2=self.speed2-10
            else:
                self.speed2=10 
   
        elif self.c==3  :
            if self.speed3 > 10:
                self.speed3=self.speed3-10
            else:
                self.speed3=10 
    #scroll functions
    def scrollx(self):
        if self.c==1 :

            pos = 0.09*self.scroll_x.value()
            self.Channel_1.plotItem.setXRange(pos,(pos+0.5))
            # self.scroll_x.setMaximum(max(self.data1))
        elif self.c==2 :

            pos = .09*self.scroll_x.value()
            self.Channel_2.plotItem.setXRange(pos,(pos+0.5))
            # self.scroll_x.setMaximum(max(self.data2))
        elif self.c==3 :

            pos = .09*self.scroll_x.value()
            self.Channel_3.plotItem.setXRange(pos,(pos+0.5))
            # self.scroll_x.setMaximum(max(self.data3))

    def scrolly(self):
        if self.c==1 :
            pos = .09*self.scroll_y.value()
            self.Channel_1.plotItem.setYRange(pos-0.5,(pos+0.05))

            
        elif self.c==2 :

            pos = .09*self.scroll_y.value()
            self.Channel_2.plotItem.setYRange(pos-0.5,(pos+0.05))
        elif self.c==3 :

            pos = .09*self.scroll_y.value()
            self.Channel_3.plotItem.setYRange(pos-0.5,(pos+0.05))
############################################################
## pdf function
    def printPDF(self):
        
        self.WIDTH = 210
        self.HEIGHT = 297
        pdf=FPDF()
        try:
            shutil.rmtree('plots')
            os.mkdir('plots')
        except FileNotFoundError:
            os.mkdir('plots')
        if self.volt1.any():
            exporter = pg.exporters.ImageExporter(self.Channel_1.plotItem)
            exporter.parameters()['width'] = self.Channel_1.plotItem.width()
            exporter.export('plots/plot-1.png')
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(40 ,10 , 'Channel_1')
            pdf.image('plots/plot-1.png', 15, 30, self.WIDTH - 30)

            if self.spectrogram1==1:
                exporter = pg.exporters.ImageExporter(self.Spectrogram_1.scene())
                exporter.export('plots/spec-1.png')
                if self.Channel_1.plotItem.height()>600 or self.Spectrogram_1.height()>600 :
                    pdf.add_page()
                    pdf.image('plots/spec-1.png' , 15, 30, self.WIDTH - 30)
                else:
                    pdf.image('plots/spec-1.png' , 15, self.WIDTH / 2 +50 , self.WIDTH - 30)
            
        if self.volt2.any():
            exporter = pg.exporters.ImageExporter(self.Channel_2.plotItem)
            exporter.parameters()['width'] = self.Channel_2.plotItem.width()
            exporter.export('plots/plot-2.png')
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(40 ,10 , 'Channel_2')
            pdf.image('plots/plot-2.png', 15, 30, self.WIDTH - 30)
            if self.spectrogram2==2:
                exporter = pg.exporters.ImageExporter(self.Spectrogram_2.scene())
                exporter.export('plots/spec-2.png')
                if self.Channel_2.plotItem.height()>600 or self.Spectrogram_2.height()>600 :
                    pdf.add_page()
                    pdf.image('plots/spec-2.png'  , 15, 30, self.WIDTH - 30)
                else:
                    pdf.image('plots/spec-2.png'  , 15, self.WIDTH / 2 + 50, self.WIDTH - 30)
            
        if self.volt3.any():
            exporter = pg.exporters.ImageExporter(self.Channel_3.plotItem)
            exporter.parameters()['width'] = self.Channel_3.plotItem.width()
            exporter.export('plots/plot-3.png')
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(40 ,10 , 'Channel_3')
            pdf.image('plots/plot-3.png', 15, 30, self.WIDTH - 30)
            if self.spectrogram3==3:
                exporter = pg.exporters.ImageExporter(self.Spectrogram_3.scene())
                exporter.export('plots/spec-3.png')
                if self.Channel_3.plotItem.height()>600 or self.Spectrogram_3.height()>600 :
                    pdf.add_page()
                    pdf.image('plots/spec-3.png' , 15, 30, self.WIDTH - 30)
                else:
                    pdf.image('plots/spec-3.png' , 15, self.WIDTH / 2 + 50, self.WIDTH - 30)
            
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf)")
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"   
        try:
            os.mkdir('pdf')
        except:
            pass
        pdf.output(f'{fn}', 'F')
        try:
            shutil.rmtree('plots')
        except:
            pass
        
        
#########################################################################################
      
    ## clear function   
    def clear(self) :
        if self.c==1 :
            self.Channel_1.clear()
            self.pause_fn()
        elif self.c==2  :
            self.Channel_2.clear()
            self.pause_fn()
             
        elif self.c==3  :
            self.Channel_3.clear()
            self.pause_fn()
        

    ## Radio_button function
    def onclicked(self):
        r=self.sender()
        if r.isChecked():
            self.c=r.value
    ## pause function
    def pause_fn (self) :
        if self.c==1 :
            self.timer1.stop()
        elif self.c==2  :
            self.timer2.stop() 
        elif self.c==3  :
            self.timer3.stop() 
    ## play function :
    def play_fn(self) :
        if self.c==1 :
            self.timer1.start()
        elif self.c==2  :
            self.timer2.start()
        elif self.c==3  :
            self.timer3.start()
    #spectrogram function:
    def generate_spectrogram1(self):
        self.spectrogram1=1
        x=self.volt1 
        f, t, Sxx = signal.spectrogram(x, 1/(self.time1[1]-self.time1[0]))
        pg.setConfigOptions(imageAxisOrder='row-major')
        p1 = self.Spectrogram_1.addPlot()
        img = pg.ImageItem()
        p1.addItem(img)
        hist =pg.HistogramLUTItem()
        hist.setImageItem(img)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, (0, 182, 188, 255)), (1.0, (246, 111, 0, 255)),
                    (0.0, (75, 0, 113, 255))]
        })
        
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        p1.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        p1.setLabel('bottom', "Time", units='s')
        p1.setLabel('left', "Frequency", units='Hz')
        self.label_Spectrogram_1.show()
        self.Spectrogram_1.show()
    def generate_spectrogram2(self):
        self.spectrogram2=2
        x=self.volt2 
        f, t, Sxx = signal.spectrogram(x,1/(self.time2[1]-self.time2[0]) )
        pg.setConfigOptions(imageAxisOrder='row-major')
        p2 = self.Spectrogram_2.addPlot()
        img = pg.ImageItem()
        p2.addItem(img)
        hist =pg.HistogramLUTItem()
        hist.setImageItem(img)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, (0, 182, 188, 255)), (1.0, (246, 111, 0, 255)),
                    (0.0, (75, 0, 113, 255))]
        })
        
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        p2.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        p2.setLabel('bottom', "Time", units='s')
        p2.setLabel('left', "Frequency", units='Hz')
        self.label_Spectrogram_2.show()
        self.Spectrogram_2.show()
    def generate_spectrogram3(self):
        self.spectrogram3=3
        x=self.volt3
        f, t, Sxx = signal.spectrogram(x, 1/(self.time3[1]-self.time3[0]))
        pg.setConfigOptions(imageAxisOrder='row-major')
        p3 = self.Spectrogram_3.addPlot()
        img = pg.ImageItem()
        p3.addItem(img)
        hist =pg.HistogramLUTItem()
        hist.setImageItem(img)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, (0, 182, 188, 255)), (1.0, (246, 111, 0, 255)),
                    (0.0, (75, 0, 113, 255))]
        })
        
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        p3.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        p3.setLabel('bottom', "Time", units='s')
        p3.setLabel('left', "Frequency", units='Hz')
        self.label_Spectrogram_3.show()
        self.Spectrogram_3.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Biosignal Viewer"))
        self.label_Channel1.setText(_translate("MainWindow", "Channel 1"))
        self.label_Channel2.setText(_translate("MainWindow", "Channel 2"))
        self.label_Channel3.setText(_translate("MainWindow", "Channel 3"))
        self.label_Spectrogram_1.setText(_translate("MainWindow", "Spectrogram 1"))
        self.label_Spectrogram_2.setText(_translate("MainWindow", "Spectrogram 2"))
        self.label_Spectrogram_3.setText(_translate("MainWindow", "Spectrogram 3"))
        self.ExitButton.setToolTip(_translate("MainWindow", "exit"))
        self.play.setToolTip(_translate("MainWindow", "play"))
        self.pause.setToolTip(_translate("MainWindow", "pause"))
        self.speed_down.setToolTip(_translate("MainWindow", "speed down"))
        self.speed_up.setToolTip(_translate("MainWindow", "speed up "))
        self.zoom_in.setToolTip(_translate("MainWindow", "zoom in "))
        self.zoom_out.setToolTip(_translate("MainWindow", "zoom out"))
        self.zoomx.setToolTip(_translate("MainWindow", "zoom x"))
        self.zoomy.setToolTip(_translate("MainWindow", "zoom y"))
        self.clear_Button.setToolTip(_translate("MainWindow", "clear"))
        self.Export.setToolTip(_translate("MainWindow", "export as pdf"))
        self.scroll_x.setToolTip(_translate("MainWindow", "scroll x"))
        self.scroll_y.setToolTip(_translate("MainWindow", "scroll y"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuGenerate.setTitle(_translate("MainWindow", "Generate"))
        self.Play_Signal_1.setText(_translate("MainWindow", "Play"))
        self.Pause_Signal_1.setText(_translate("MainWindow", "Pause"))
        self.Clear_Signal_1.setText(_translate("MainWindow", "Clear"))
        self.Play_Signal_2.setText(_translate("MainWindow", "Play"))
        self.Pause_Signal_2.setText(_translate("MainWindow", "Pause"))
        self.Clear_Signal_2.setText(_translate("MainWindow", "Clear"))
        self.Play_Signal_3.setText(_translate("MainWindow", "Play"))
        self.Pause_Signal_3.setText(_translate("MainWindow", "Pause"))
        self.Clear_Signal_3.setText(_translate("MainWindow", "Clear"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionOpen_3.setText(_translate("MainWindow", "Open"))
        self.OpenChannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.OpenChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.OpenChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.zoom_x_Signal_1.setText(_translate("MainWindow", "Signal 1"))
        self.zoom_x_Signal_2.setText(_translate("MainWindow", "Signal 2"))
        self.zoom_x_Signal_3.setText(_translate("MainWindow", "Signal 3"))
        self.zoom_y_Signal_1.setText(_translate("MainWindow", "Signal 1"))
        self.zoom_y_Signal_2.setText(_translate("MainWindow", "Signal 2"))
        self.zoom_y_Signal_3.setText(_translate("MainWindow", "Signal 3"))
        self.Export_Signal_1.setText(_translate("MainWindow", "Export Signal 1"))
        self.Export_Signal_2.setText(_translate("MainWindow", "Export Signal 2"))
        self.Export_Signal_3.setText(_translate("MainWindow", "Export Signal 3"))
        self.Signal_1_Spectrogram.setText(_translate("MainWindow", "Signal 1 Spectrogram"))
        self.Signal_2_Spectrogram.setText(_translate("MainWindow", "Signal 2 Spectrogram"))
        self.Signal_3_Spectrogram.setText(_translate("MainWindow", "Signal 3 Spectrogram"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_X.setText(_translate("MainWindow", "Zoom X"))
        self.actionZoom_Y.setText(_translate("MainWindow", "Zoom Y"))


        self.r1.setShortcut(_translate("MainWindow", "1"))
        self.r2.setShortcut(_translate("MainWindow", "2"))
        self.r3.setShortcut(_translate("MainWindow", "3"))
        self.ExitButton.setShortcut(_translate("MainWindow", "Esc"))
        self.play.setShortcut(_translate("MainWindow", "P"))
        self.pause.setShortcut(_translate("MainWindow", "S"))
        self.speed_down.setShortcut(_translate("MainWindow", "D"))
        self.speed_up.setShortcut(_translate("MainWindow", "U"))
        self.zoom_in.setShortcut(_translate("MainWindow", "+"))
        self.zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.zoomx.setShortcut(_translate("MainWindow", "X"))
        self.zoomy.setShortcut(_translate("MainWindow", "Y"))
        self.clear_Button.setShortcut(_translate("MainWindow", "Backspace"))
        self.Export.setShortcut(_translate("MainWindow", "E"))
        self.OpenChannel_1.setShortcut(_translate("MainWindow", "O, 1"))
        self.OpenChannel_2.setShortcut(_translate("MainWindow", "O, 2"))
        self.OpenChannel_3.setShortcut(_translate("MainWindow", "O, 3"))
        self.Signal_1_Spectrogram.setShortcut(_translate("MainWindow", "G, 1"))
        self.Signal_2_Spectrogram.setShortcut(_translate("MainWindow", "G, 2"))
        self.Signal_3_Spectrogram.setShortcut(_translate("MainWindow", "G, 3"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
