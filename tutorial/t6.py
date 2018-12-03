#!/usr/bin/env python
# encoding: utf-8
# t6.py in PyQt5
# Created by maverick on 2018/12/3, 5:24 PM
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t6.py
@time: 2018/12/3 5:24 PM
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        lcd: QtWidgets.QLCDNumber = QtWidgets.QLCDNumber(2)

        slider: QtWidgets.QSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)
        slider.valueChanged.connect(lcd.display)

        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        quit: QtWidgets.QPushButton = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        quit.clicked.connect(QtWidgets.qApp.quit)

        grid: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(quit)
        self.setLayout(layout)

        for row in range(3):
            for col in range(3):
                grid.addWidget(LCDRange(), row, col)





if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

    widget: MyWidget = MyWidget()
    widget.show()

    sys.exit(app.exec_())