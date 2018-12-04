#!/usr/bin/env python
# encoding: utf-8
# t7.py in PyQt5
# Created by maverick on 2018-12-04, 12:56
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t7.py
@time: 2018-12-04 12:56
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class LCDRange(QtWidgets.QWidget):

    valueChanged = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        lcd: QtWidgets.QLCDNumber = QtWidgets.QLCDNumber(2)

        self.slider: QtWidgets.QSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0, 99)
        self.slider.setValue(0)

        self.slider.valueChanged.connect(lcd.display)
        self.slider.valueChanged.connect(self.valueChanged)   # connect to self signal

        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def value(self):
        return self.slider.value()

    @QtCore.pyqtSlot(int)
    def setValue(self, value):
        self.slider.setValue(value)

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        quit: QtWidgets.QPushButton = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times",
                                 18,
                                 QtGui.QFont.Bold))
        quit.clicked.connect(QtWidgets.qApp.quit)

        grid: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        previousRange = None

        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(quit)
        self.setLayout(layout)

        for row in range(3):
            for col in range(3):
                lcdRange: LCDRange = LCDRange()
                grid.addWidget(lcdRange, row, col)

                if previousRange:
                    lcdRange.valueChanged.connect(previousRange.setValue)

                previousRange = lcdRange


if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

    widget: MyWidget = MyWidget()
    widget.show()
    sys.exit(app.exec_())