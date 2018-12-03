#!/usr/bin/env python
# encoding: utf-8
# t5.py in PyQt5
# Created by maverick on 2018/12/3, 4:41 PM
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t5.py
@time: 2018/12/3 4:41 PM
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        quit: QtWidgets.QPushButton = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        lcd: QtWidgets.QLCDNumber = QtWidgets.QLCDNumber(2)

        slider: QtWidgets.QSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)

        quit.clicked.connect(QtWidgets.qApp.quit)
        slider.valueChanged.connect(lcd.display)

        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()

        layout.addWidget(lcd)
        layout.addWidget(slider)
        layout.addWidget(quit)

        self.setLayout(layout)


if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

    # do sth
    widget: MyWidget = MyWidget()
    widget.show()

    sys.exit(app.exec_())