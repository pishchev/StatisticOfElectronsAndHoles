# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg


class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(1282, 462)
        Application.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(Application)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Ed_silder = QtWidgets.QSlider(self.centralwidget)
        self.Ed_silder.setMinimumSize(QtCore.QSize(150, 50))
        self.Ed_silder.setMaximum(112)
        self.Ed_silder.setOrientation(QtCore.Qt.Horizontal)
        self.Ed_silder.setObjectName("Ed_silder")
        self.horizontalLayout_3.addWidget(self.Ed_silder)
        self.Ed_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ed_lineEdit.sizePolicy().hasHeightForWidth())
        self.Ed_lineEdit.setSizePolicy(sizePolicy)
        self.Ed_lineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.Ed_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.Ed_lineEdit.setReadOnly(True)
        self.Ed_lineEdit.setObjectName("Ed_lineEdit")
        self.horizontalLayout_3.addWidget(self.Ed_lineEdit)
        self.Ed_label = QtWidgets.QLabel(self.centralwidget)
        self.Ed_label.setObjectName("Ed_label")
        self.horizontalLayout_3.addWidget(self.Ed_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Nd0_slider = QtWidgets.QSlider(self.centralwidget)
        self.Nd0_slider.setMinimumSize(QtCore.QSize(150, 50))
        self.Nd0_slider.setMinimum(1)
        self.Nd0_slider.setMaximum(7)
        self.Nd0_slider.setSingleStep(1)
        self.Nd0_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Nd0_slider.setObjectName("Nd0_slider")
        self.horizontalLayout_5.addWidget(self.Nd0_slider)
        self.Nd0_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Nd0_lineEdit.sizePolicy().hasHeightForWidth())
        self.Nd0_lineEdit.setSizePolicy(sizePolicy)
        self.Nd0_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.Nd0_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.Nd0_lineEdit.setReadOnly(True)
        self.Nd0_lineEdit.setObjectName("Nd0_lineEdit")
        self.horizontalLayout_5.addWidget(self.Nd0_lineEdit)
        self.Nd0_label = QtWidgets.QLabel(self.centralwidget)
        self.Nd0_label.setObjectName("Nd0_label")
        self.horizontalLayout_5.addWidget(self.Nd0_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.T_slider = QtWidgets.QSlider(self.centralwidget)
        self.T_slider.setMinimumSize(QtCore.QSize(150, 50))
        self.T_slider.setMinimum(10)
        self.T_slider.setMaximum(400)
        self.T_slider.setOrientation(QtCore.Qt.Horizontal)
        self.T_slider.setObjectName("T_slider")
        self.horizontalLayout_6.addWidget(self.T_slider)
        self.T1_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T1_lineEdit.sizePolicy().hasHeightForWidth())
        self.T1_lineEdit.setSizePolicy(sizePolicy)
        self.T1_lineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.T1_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.T1_lineEdit.setReadOnly(True)
        self.T1_lineEdit.setObjectName("T1_lineEdit")
        self.horizontalLayout_6.addWidget(self.T1_lineEdit)
        self.T_label = QtWidgets.QLabel(self.centralwidget)
        self.T_label.setObjectName("T_label")
        self.horizontalLayout_6.addWidget(self.T_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 3, 1)
        styles = {'color': 'r', 'font-size': '15px', 'font-weight': 'bold'}

        fnt = QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        self.plot1 = PlotWidget(self.centralwidget)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        self.plot1.getAxis("bottom").setTickFont(fnt)
        self.plot1.getAxis("left").setTickFont(fnt)
        self.plot1.setMinimumSize(QtCore.QSize(200, 200))
        self.plot1.setObjectName("plot1")
        self.gridLayout.addWidget(self.plot1, 0, 0, 1, 2)
        self.plot1.getAxis("left").enableAutoSIPrefix(False)
        self.plot1.setLabel('left', 'Concentration', **styles)
        self.plot1.setLabel('bottom', 'Temperature, K', **styles)

        self.plot2 = PlotWidget(self.centralwidget)
        self.plot2.setMinimumSize(QtCore.QSize(200, 200))
        self.plot2.setObjectName("plot2")
        self.plot2.getAxis("bottom").setTickFont(fnt)
        self.plot2.getAxis("left").setTickFont(fnt)

        self.plot2.setLabel('left', 'Fermi level, eV', **styles)
        self.plot2.setLabel('bottom', 'Temperature, K', **styles)

        self.gridLayout.addWidget(self.plot2, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        Application.setCentralWidget(self.centralwidget)

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)
        self.plot1.setBackground('w')
        self.plot2.setBackground('w')

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "SOEAH"))
        self.Ed_label.setText(_translate("Application", "E_d"))
        self.Nd0_label.setText(_translate("Application", "N_d0"))
        self.T_label.setText(_translate("Application", "T"))
