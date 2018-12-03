#!/usr/bin/env python
# encoding: utf-8
# t2.py in PyQt5
# Created by maverick on 2018/12/3, 3:56 PM
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t2.py
@time: 2018/12/3 3:56 PM
"""

import sys
from PyQt5 import QtCore, QtWidgets, QtGui

# Step 1: init:
app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

# Step 2: do sth:
quit: QtWidgets.QPushButton = QtWidgets.QPushButton("Quit")
quit.resize(QtCore.QSize(75, 30))
quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

# !new Signal-Slot connection
quit.clicked.connect(app.quit)


# Step 1+: close:
quit.show()
sys.exit(app.exec_())
