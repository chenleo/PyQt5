#!/usr/bin/env python
# encoding: utf-8
# t4.py in PyQt5
# Created by maverick on 2018/12/3, 4:30 PM
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t4.py
@time: 2018/12/3 4:30 PM
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


# Self define widget
class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.setFixedSize(QtCore.QSize(200, 120))

        self.quit: QtWidgets.QPushButton = QtWidgets.QPushButton("Quit", parent=self)
        self.quit.setGeometry(QtCore.QRect(62, 40, 75, 30))
        self.quit.setFont(QtGui.QFont("Times",
                                      18,
                                      QtGui.QFont.Bold))
        self.quit.clicked.connect(QtWidgets.qApp.quit)                 # connect to a global quit




# step 1: Bound Together!
if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

    # do sth
    widget: MyWidget = MyWidget()
    widget.show()

    sys.exit(app.exec_())