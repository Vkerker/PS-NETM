from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import pandas as pd

from PSNETM_readcoords import *
from PSNETM_filters import *
from PSNETM_statistical_analysis import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(1500, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_frame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy)
        self.left_frame.setMinimumWidth(150)
        self.left_frame.setMaximumWidth(180)
        self.left_frame.setObjectName("left_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.left_frame)
        font = QtGui.QFont('Segoe UI')
        font.setPointSize(10)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.HorizontalLine = QtWidgets.QFrame(self.left_frame)
        self.HorizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.HorizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(self.HorizontalLine)
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.left_frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.font = QtGui.QFont('Segoe UI')
        self.font.setPointSize(9)
        self.comboBox_2.setFont(self.font)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setVisible(False)
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.label = QtWidgets.QLabel(self.left_frame)
        self.label.setVisible(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont('Segoe UI')
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalWidget = QtWidgets.QWidget(self.left_frame)
        self.horizontalWidget.setVisible(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        font = QtGui.QFont('Segoe UI')
        font.setPointSize(9)

        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setFont(font)
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setFont(font)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        font = QtGui.QFont('Segoe UI')
        font.setPointSize(9)
        self.filter_button = QtWidgets.QPushButton(self.left_frame)
        self.filter_button.setVisible(False)
        self.filter_button.setFont(font)
        self.clear_canvas_button = QtWidgets.QPushButton(self.left_frame)
        self.clear_canvas_button.setEnabled(False)
        self.clear_canvas_button.setFont(font)
        self.HorizontalLine = QtWidgets.QFrame(self.left_frame)
        self.HorizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.HorizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(self.filter_button)
        self.verticalLayout_2.addWidget(self.HorizontalLine)
        self.verticalLayout_2.addWidget(self.clear_canvas_button)
        self.horizontalLayout.addWidget(self.left_frame, 0, QtCore.Qt.AlignTop)

        self.midFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midFrame.sizePolicy().hasHeightForWidth())
        self.midFrame.setSizePolicy(sizePolicy)
        self.midFrame.setMinimumWidth(700)
        self.midFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.midFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.midFrame.setObjectName("midFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.midFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        font = QtGui.QFont('Segoe UI')
        font.setPointSize(9)

        self.tabWidget = QtWidgets.QTabWidget(self.midFrame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.setFont(font)

        self.Hist_layout = QtWidgets.QVBoxLayout(self.tab)
        self.Hist_layout.setContentsMargins(0, 0, 0, 0)
        self.Hist_layout.setSpacing(0)
        self.Hist_layout.setObjectName("Hist_layout")     
        
        self.Hist_Figure = Figure()
        self.NHaxs = self.Hist_Figure.add_subplot(311)
        self.EHaxs = self.Hist_Figure.add_subplot(312)
        self.UHaxs = self.Hist_Figure.add_subplot(313)
        self.Hist_Figure.tight_layout()
        self.Hist_Canvas = FigureCanvas(self.Hist_Figure)

        self.Hist_toolbar = NavigationToolbar(self.Hist_Canvas)
        self.Hist_layout.addWidget(self.Hist_Canvas)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.TSPlot_layout = QtWidgets.QVBoxLayout(self.tab_2)
        self.TSPlot_layout.setContentsMargins(0, 0, 0, 0)
        self.TSPlot_layout.setSpacing(0)
        self.TSPlot_layout.setObjectName("TSPlot_Layout")

        self.TSPlot_Figure = Figure()
        self.NTaxs = self.TSPlot_Figure.add_subplot(311)
        self.ETaxs = self.TSPlot_Figure.add_subplot(312, sharex=self.NTaxs)
        self.UTaxs = self.TSPlot_Figure.add_subplot(313, sharex=self.NTaxs)
        self.TSPlot_Figure.tight_layout()
        self.TSPlot_Canvas = FigureCanvas(self.TSPlot_Figure)
        
        self.TStoolbar = NavigationToolbar(self.TSPlot_Canvas)
        self.TSPlot_layout.addWidget(self.TSPlot_Canvas)

        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.midFrame)
        self.rightFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy)
        self.rightFrame.setMinimumWidth(480)
        self.rightFrame.setMaximumWidth(480)
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.table_label = QtWidgets.QLabel(self.rightFrame)
        self.table_label.setText("Statistical parameters")
        self.table_label.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        font = QtGui.QFont('Segoe UI')
        font.setPointSize(12)
        font.setWeight(75)
        self.table_label.setMaximumHeight(24)
        self.table_label.setFont(font)
        self.table_label.setSizePolicy(sizePolicy)
        self.verticalLayout_4.addWidget(self.table_label)

        self.tableWidget = QtWidgets.QTableWidget(self.rightFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setFixedHeight(365)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(9)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        

        self.label2 = QtWidgets.QLabel(self.rightFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.label2.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont('Segoe UI')
        font.setPointSize(12)
        font.setWeight(75)
        self.label2.setSizePolicy(sizePolicy)
        self.label2.setFont(font)

        self.horizontalWidget1 = QtWidgets.QWidget(self.rightFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy)
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        font = QtGui.QFont('Segoe UI')
        font.setPointSize(9)
        font.setWeight(65)
        
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_3.setText('N')
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_4.setText('E')
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_5.setText('U')
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)

        self.HorizontalLine2 = QtWidgets.QFrame(self.rightFrame)
        self.HorizontalLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.HorizontalLine2.setFrameShadow(QtWidgets.QFrame.Sunken)

        font = QtGui.QFont('Segoe UI')
        font.setPointSize(12)
        self.label_6 = QtWidgets.QLabel(self.rightFrame)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setTextInteractionFlags(self.label_6.textInteractionFlags() | QtCore.Qt.TextSelectableByMouse)
        self.label_6.setObjectName("label_2")
        self.label_6.setAlignment(QtCore.Qt.AlignTop)
            
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_4.addWidget(self.label2)
        self.verticalLayout_4.addWidget(self.horizontalWidget1)
        self.verticalLayout_4.addWidget(self.HorizontalLine2)
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout.addWidget(self.rightFrame)
        self.verticalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder.setObjectName("actionOpen_folder")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionExport_conclusion = QtWidgets.QAction(MainWindow)
        self.actionExport_conclusion.setObjectName("actionExport_conclusion")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName('actionExit')

        self.menuFile.addAction(self.actionOpen_folder)
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_conclusion)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.TSPlot_layout.addWidget(self.TStoolbar)
        self.Hist_layout.addWidget(self.Hist_toolbar)

        self.actionOpen_folder.triggered.connect(self.open_folder)
        self.actionOpen_file.triggered.connect(self.open_file)
        self.actionExit.triggered.connect(QtCore.QCoreApplication.quit)

        self.checkBox_3.toggled.connect(self.filter_button.setVisible)
        self.checkBox_3.toggled.connect(self.comboBox_2.setVisible)
        self.checkBox_3.toggled.connect(self.update_filter_options)
        self.checkBox_3.toggled.connect(lambda checked: self.clear_filtered(checked))

        self.filter_button.clicked.connect(lambda: self.filter_coordinates(self.coordinates, self.comboBox_2.currentText()))
        self.comboBox_2.currentIndexChanged.connect(self.update_filter_options)

        self.clear_canvas_button.clicked.connect(self.clear_canvas)

        self.actionExport_conclusion.triggered.connect(self.export_conclusion)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PS-NETM"))
        self.checkBox_3.setText(_translate("MainWindow", "Filter time series"))
        self.clear_canvas_button.setText(_translate("MainWindow", "Clear"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Wavelet filter"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "EMD filter"))
        
        self.label.setText(_translate("MainWindow", "Filter options"))
        self.label2.setText(_translate("MainWindow", "NETM Conclusions"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "5"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Time series"))
        
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "cA"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "cE"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "p(\u03c7\u00B2)"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "D(n)"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "n"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "RMS"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "File name"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "U"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionExit.setText(_translate('MainWindow', 'Exit'))
        self.actionOpen_folder.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExport_conclusion.setText(_translate("MainWindow", "Export conclusion"))
        self.filter_button.setText(_translate("MainWindow", "Apply filter"))

    #Responsible for handling folders with Pride PPP-AR *_pos files
    def open_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "Select a folder")
        if path == "" : return
        try:
            coordinates, self.stname = prideppp_read(path)
        except PermissionError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Chosen folder contains subfolders. Please choose another folder.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Chosen folder contains files, other than Pride-PPPAR pos files.\nPlease choose another folder.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        if len(coordinates.loc[:, "N"]) < 500:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Chosen folder contains less than 500 observations. Results might be inadequate.\nRefer to the manual for more information.")
            msg.setWindowTitle("Error")
            msg.exec_()
        
        coordinates = remove_outliers(coordinates)

        coordinates, self.slope = remove_secular_trend(coordinates)

        self.coordinates = resample_coords(coordinates)

        self.clear_canvas()
        self.plot_Hist(self.coordinates)
        self.plot_input_graph(self.coordinates)
        self.clear_canvas_button.setEnabled(True)
        self.checkBox_3.setEnabled(True)

    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Select a file")
        if path == "" :
            return
        elif path[-4:] == ".neu" or path[-4:] == ".NEU":
            coordinates = NEU_read(path)
            self.stname = path.split("/")[-1]
        elif path[-7:] == ".series":
            coordinates = series_read(path)
            self.stname = path.split("/")[-1]
        elif path[-4:] == ".XYZ" or path[-4:] == ".xyz":
            coordinates = XYZ_read(path)
            self.stname = path.split("/")[-1]
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Chosen format is not supported.\nPlease choose another file.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        if len(coordinates.loc[:, "N"]) < 500:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Chosen file contains less than 500 observations. Results might be inadequate.\nPlease, refer to the manual for more information.")
            msg.setWindowTitle("Error")
            msg.exec_()
        
        coordinates = remove_outliers(coordinates)

        coordinates = resample_coords(coordinates)

        self.coordinates, self.slope = remove_secular_trend(coordinates)

        self.clear_canvas()
        self.plot_Hist(self.coordinates)
        self.plot_input_graph(self.coordinates)
        
        self.clear_canvas_button.setEnabled(True)
        self.checkBox_3.setEnabled(True)

    #Responsible for plotting histograms
    def plot_Hist(self, data):

        n = len(data["N"])
        weights = np.ones_like(data["N"]) / len(data["N"])
        bins = round(1 + 3.322*np.log10(n))
        hist_label = str('Number of bins: ' + str(bins) + '\nDegrees of freedom: ' + str(bins - 3))

        self.NHaxs.clear()
        self.EHaxs.clear()
        self.UHaxs.clear()

        kN, valsN, patchesN = self.NHaxs.hist(data["N"], bins=bins, weights=weights, alpha = 0.5, edgecolor = "black")
        self.NHaxs.axvline(x=0, color="red")
        self.NHaxs.bar_label(patchesN, fontsize=10, fmt="%.2f", label_type="center", padding=3)
        self.NHaxs.text(0.1, 0.8, hist_label, ha='left', va='center', transform=self.NHaxs.transAxes, fontsize=10)
        self.NHaxs.set_title(f'Histogram of North-coordinate')
        self.NHaxs.set_ylabel('Frequency')
        
        kE, valsE, patchesE = self.EHaxs.hist(data["E"], bins=bins, weights=weights, alpha = 0.5, edgecolor = "black")
        self.EHaxs.axvline(x=0, color="red")
        self.EHaxs.bar_label(patchesE, fontsize=10, fmt="%.2f", label_type="center", padding=3)
        self.EHaxs.text(0.1, 0.8, hist_label, ha='left', va='center', transform=self.EHaxs.transAxes, fontsize=10)
        self.EHaxs.set_title(f'Histogram of East-coordinate')
        self.EHaxs.set_ylabel('Frequency')
        
        kU, valsU, patchesU = self.UHaxs.hist(data["U"], bins=bins, weights=weights, alpha = 0.5, edgecolor = "black")
        self.UHaxs.axvline(x=0, color="red")
        self.UHaxs.bar_label(patchesU, fontsize=10, fmt="%.2f", label_type="center", padding=3)
        self.UHaxs.text(0.1, 0.8, hist_label, ha='left', va='center', transform=self.UHaxs.transAxes, fontsize=10)
        self.UHaxs.set_title(f'Histogram of Up-coordinate')
        self.UHaxs.set_ylabel('Frequency')

        self.Hist_Canvas.draw()

    #Responsible for plotting unfiltered time series
    def plot_input_graph(self, data):
        self.NTaxs.axhline(y=0, color = "red")
        self.input_NT, = self.NTaxs.plot(data.index, data["N"], label = "Input")
        self.NTaxs.set_title(f'Time series of North-coordinate')
        self.NTaxs.text(0.18, 0.1, "Trend slope: " + str(round(self.slope['N']['slope'] * 365.25 * 1000, 2)) + " mm/year", ha='center', va='center', transform=self.NTaxs.transAxes, fontsize=10)

        self.ETaxs.axhline(y=0, color = "red")
        self.input_ET, = self.ETaxs.plot(data.index, data["E"], label = "Input")
        self.ETaxs.set_title(f'Time series of East-coordinate')
        self.ETaxs.text(0.18, 0.1, "Trend slope: " + str(round(self.slope['E']['slope'] * 365.25 * 1000, 2)) + " mm/year", ha='center', va='center', transform=self.ETaxs.transAxes, fontsize=10)

        self.UTaxs.axhline(y=0, color = "red")
        self.input_UT, = self.UTaxs.plot(data.index, data["U"], label = "Input")
        self.UTaxs.set_title(f'Time series of Up-coordinate')
        self.UTaxs.text(0.18, 0.1, "Trend slope: " + str(round(self.slope['U']['slope'] * 365.25 * 1000, 2)) + " mm/year", ha='center', va='center', transform=self.UTaxs.transAxes, fontsize=10)

        self.TSPlot_Canvas.draw()

    #Responsible for plotting filtered TS
    def plot_filtered_graph(self, data):
        if not hasattr(self, "filtered_NT"):

            self.filtered_NT, = self.NTaxs.plot(data.index, data["N"], label = "Filtered", color = 'orange')
            self.filtered_ET, = self.ETaxs.plot(data.index, data["E"], label = "Filtered", color = 'orange')
            self.filtered_UT, = self.UTaxs.plot(data.index, data["U"], label = "Filtered", color = 'orange')
            self.NTaxs.legend()
            self.ETaxs.legend()
            self.UTaxs.legend()

        else:

            self.filtered_NT.set_xdata(data.index)
            self.filtered_NT.set_ydata(data["N"])

            self.filtered_ET.set_xdata(data.index)
            self.filtered_ET.set_ydata(data["E"])

            self.filtered_UT.set_xdata(data.index)
            self.filtered_UT.set_ydata(data["U"])

        self.TSPlot_Canvas.draw()      

    #Responsible for filtering TS, depending on selected options
    def filter_coordinates(self, data, filter):
        if filter == "Wavelet filter":
            wt = self.comboBox_3.currentText()
            level = int(self.comboBox_4.currentText())
            filtered_coords = wavelet_denoise(data, wt, level)
        elif filter == "EMD filter":
            filtered_coords = emd_denoise(data)
                
        self.plot_filtered_graph(filtered_coords)
        self.plot_Hist(filtered_coords)
        self.NETM(filtered_coords)
        self.update_table()
        self.update_conclusions()
    
    #Adds some options, if filter == 'Wavelet'
    def update_filter_options(self):
        if self.comboBox_2.currentIndex() == 0:
            self.label.setVisible(True)
            self.horizontalWidget.setVisible(True)
            
            self.comboBox_3.setItemText(0, "sym4")
            self.comboBox_3.setItemText(1, "db4")

            self.comboBox_4.setItemText(0,"1")
            self.comboBox_4.setItemText(1,"2")
            self.comboBox_4.setItemText(2,"3")
            self.comboBox_4.setItemText(3,"4")
            self.comboBox_4.setItemText(4,"5")
            

        elif self.comboBox_2.currentIndex() == 1:
            self.label.setVisible(False)
            self.horizontalWidget.setVisible(False)
            
    
    #Removes filtered TS and clears table if 'Filter coordinates' is unchecked
    def clear_filtered(self, checked):
        if checked:
            return
        else:
            try:
                self.horizontalWidget.setVisible(False)
                self.label.setVisible(False)
                self.filtered_NT.remove()
                self.filtered_ET.remove()
                self.filtered_UT.remove()

                self.NTaxs.legend()
                self.ETaxs.legend()
                self.UTaxs.legend()
                
                del self.filtered_NT
                del self.filtered_ET
                del self.filtered_UT

            except: return

            self.TSPlot_Canvas.draw()
            
            self.label.setVisible(False)
            self.horizontalWidget.setVisible(False)

            self.table_set_clear()
            self.label_3.setStyleSheet("background-color: none")
            self.label_4.setStyleSheet("background-color: none")
            self.label_5.setStyleSheet("background-color: none")
            self.label_6.setText('')
            
    #Responsible for clearing all information, that is present on screen
    def clear_canvas(self):
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setEnabled(False)

        self.NHaxs.clear()
        self.EHaxs.clear()
        self.UHaxs.clear()

        self.NHaxs.relim()
        self.EHaxs.relim()
        self.UHaxs.relim()

        self.Hist_Canvas.draw()

        self.NTaxs.clear()
        self.ETaxs.clear()
        self.UTaxs.clear()

        self.NTaxs.relim()
        self.ETaxs.relim()
        self.UTaxs.relim()

        self.TSPlot_Canvas.draw()

        self.table_set_clear()
        self.label_3.setStyleSheet("background-color: none")
        self.label_4.setStyleSheet("background-color: none")
        self.label_5.setStyleSheet("background-color: none")

        self.label.setVisible(False)
        self.filter_button.setVisible(False)
        self.comboBox_2.setVisible(False)
        self.horizontalWidget.setVisible(False)

    #Clears table
    def table_set_clear(self): 
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setText("")
                self.tableWidget.setItem(row, column, item)

    #Performs NETM analysis
    def NETM(self, data):
        self.A, self.E, self.m, self.sigA, self.sigE, self.confA, self.confE, self.n = NETM(data)
        intervals, x_i, m_i = hist_data(data, self.n)
        self.Pierson, m_x, dispers = p_criteria(x_i, m_i, self.n, intervals)
        self.Kolmogorov = k_criteria(m_i, intervals, self.n, m_x, dispers)

    #Responsible for exporting data to .txt file
    def export_conclusion(self):
        path,_ = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Select a folder", "", "Text files (*.txt)")
        exported_data = pd.concat([self.A, self.E, self.m, self.sigA, self.sigE, self.confA, self.confE, self.Pierson, self.Kolmogorov], axis=0)
        labels = ['Skewness', 'Kurtosis', 'm2', 'm3', 'm4', 'm5', 'm6', 'm8', 'RMS' ,'sigA', 'sigE', 'Confidence interval A (lower)', 'Confidence interval A (higher)', 'Confidence interval E (lower)', 'Confidence interval E (higher)', 'Pierson chi2', 'Kolmogorov D(n)']
        exported_data.index = labels
        exported_data.to_csv(path, sep='\t', encoding='utf-8')

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Export completed successfully!")
        msg.setWindowTitle("Success")
        msg.exec_()

    #Responsible for creating conclusion, based on NETM
    def update_conclusions(self):
        g=0
        y=0
        r=0
        for col in self.coordinates.columns:
            if self.confA.loc[0, col] < 0 and self.confA.loc[1, col] > 0 and self.confE.loc[0, col] < 0 and self.confE.loc[1, col] > 0:
                g+=1
                if col == "N":
                    self.label_3.setStyleSheet("background-color: rgba(56, 255, 56, 85);")
                elif col == "E":
                    self.label_4.setStyleSheet("background-color: rgba(56, 255, 56, 85);")
                elif col == "U":
                    self.label_5.setStyleSheet("background-color: rgba(56, 255, 56, 85);")

                #self.label_6.setText('There`s no need to use NETM methods.')

            elif self.confA.loc[0, col] < 0 and self.confA.loc[1, col] > 0 and self.confE.loc[1, col] <= 6:
                y+=1
                if col == "N":
                    self.label_3.setStyleSheet("background-color: rgba(255, 142, 85, 75);")
                elif col == "E":
                    self.label_4.setStyleSheet("background-color: rgba(255, 142, 85, 75);")
                elif col == "U":
                    self.label_5.setStyleSheet("background-color: rgba(255, 142, 85, 75);")

                #self.label_6.setText('There is an effect of weak systematic errors that were not excluded when processing GNSS observations. Evaluation by NETM methods is required.')

            else:
                r+=1
                if col == "N":
                    self.label_3.setStyleSheet("background-color: rgba(242, 26, 26, 90);")
                elif col == "E":
                    self.label_4.setStyleSheet("background-color: rgba(242, 26, 26, 90);")
                elif col == "U":
                    self.label_5.setStyleSheet("background-color: rgba(242, 26, 26, 90);")
                    

                #self.label_6.setText('Significant data pathology. Evaluation is not possible.')

        if g == 3:
            self.label_6.setText('There`s no need to use NETM methods.')
        elif y >= 2 and r==0 or g==2 and r == 0:
            self.label_6.setText('There is an effect of weak systematic errors that were not excluded when processing GNSS observations. Evaluation by NETM methods is required.')
        else:
            self.label_6.setText('Significant data pathology. Evaluation is not possible.')
                
    #Responsible for handling table widget
    def update_table(self):
        self.tableWidget.item(0, 0).setText(str(self.A.loc[0, "N"]) + " ± " + str(self.sigA.loc[0, "N"]))
        self.tableWidget.item(0, 1).setText(str(self.A.loc[0, "E"]) + " ± " + str(self.sigA.loc[0, "E"]))
        self.tableWidget.item(0, 2).setText(str(self.A.loc[0, "U"]) + " ± " + str(self.sigA.loc[0, "U"]))

        self.tableWidget.item(1, 0).setText(str(self.E.loc[0, "N"]) + " ± " + str(self.sigE.loc[0, "N"]))
        self.tableWidget.item(1, 1).setText(str(self.E.loc[0, "E"]) + " ± " + str(self.sigE.loc[0, "E"]))
        self.tableWidget.item(1, 2).setText(str(self.E.loc[0, "U"]) + " ± " + str(self.sigE.loc[0, "U"]))

        self.tableWidget.item(2, 0).setText(str(self.confA.loc[0, "N"]) + " , " + str(self.confA.loc[1, "N"]))
        self.tableWidget.item(2, 1).setText(str(self.confA.loc[0, "E"]) + " , " + str(self.confA.loc[1, "E"]))
        self.tableWidget.item(2, 2).setText(str(self.confA.loc[0, "U"]) + " , " + str(self.confA.loc[1, "U"]))

        self.tableWidget.item(3, 0).setText(str(self.confE.loc[0, "N"]) + " , " + str(self.confE.loc[1, "N"]))
        self.tableWidget.item(3, 1).setText(str(self.confE.loc[0, "E"]) + " , " + str(self.confE.loc[1, "E"]))
        self.tableWidget.item(3, 2).setText(str(self.confE.loc[0, "U"]) + " , " + str(self.confE.loc[1, "U"]))

        self.tableWidget.item(4, 0).setText(str(self.Pierson.loc[0, "N"]))
        self.tableWidget.item(4, 1).setText(str(self.Pierson.loc[0, "E"]))
        self.tableWidget.item(4, 2).setText(str(self.Pierson.loc[0, "U"]))

        self.tableWidget.item(5, 0).setText(str(self.Kolmogorov.loc[0, "N"]))
        self.tableWidget.item(5, 1).setText(str(self.Kolmogorov.loc[0, "E"]))
        self.tableWidget.item(5, 2).setText(str(self.Kolmogorov.loc[0, "U"]))

        self.tableWidget.item(6, 0).setText(str(self.n))
        self.tableWidget.item(6, 1).setText(str(self.n))
        self.tableWidget.item(6, 2).setText(str(self.n))

        self.tableWidget.item(7, 0).setText(str(round(self.m.loc['RMS', 'N'] * 1000, 2)))
        self.tableWidget.item(7, 1).setText(str(round(self.m.loc['RMS', 'E'] * 1000, 2)))
        self.tableWidget.item(7, 2).setText(str(round(self.m.loc['RMS', 'U'] * 1000, 2)))

        self.tableWidget.item(8, 0).setText(str(self.stname))
        self.tableWidget.item(8, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setSpan(8, 0, 1, 3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setWindowIcon(QtGui.QIcon('resources/icon_256.png'))
    MainWindow.setWindowIcon(QtGui.QIcon('resources/icon_256.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
