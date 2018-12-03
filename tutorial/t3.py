#!/usr/bin/env python
# encoding: utf-8
# t3.py in PyQt5
# Created by maverick on 2018/12/3, 4:07 PM
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t3.py
@time: 2018/12/3 4:07 PM
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


# Step 1: init
app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

# Step 2: do sth
window: QtWidgets.QWidget = QtWidgets.QWidget()
window.resize(QtCore.QSize(200, 120))

quit: QtWidgets.QPushButton = QtWidgets.QPushButton(text="Quit", parent=window)
quit.setFont(QtGui.QFont("Times",                     # family can not be used
                         pointSize=18,
                         weight=QtGui.QFont.Bold,
                         italic=False))
quit.setGeometry(QtCore.QRect(10, 40, 180, 40))
quit.clicked.connect(app.quit)

# Step 1+: close
window.show()
sys.exit(app.exec_())